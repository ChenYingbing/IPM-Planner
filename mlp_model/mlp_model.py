import torch
import random
import numpy as np
import torch.nn as nn
import torch.optim as optim
import networks.torchbnn as bnn
import os
import torch.nn.functional as F

# Function: InteractionPriorityModel().forward(M^-, M^+)
# Return: P(\Delta t < 0 | M^-, M^+)
#
# Models: (CPU device)
#   ipmodel.ckpt: torch.save()
#   ipmodel.pt:   torch.jit.script().save()
class InteractionPriorityModel():
    def __init__(self, device, file_dir, 
                 input_dim=2, midlayer_dim=5, output_dim=2) -> None:
      self.device = device
      self.file_dir = file_dir
      self.model_file = os.path.join(file_dir, "ipmodel.ckpt")
      self.script_model_file = os.path.join(file_dir, "ipmodel.pt")

      self.initial_loss = None

      # network
      self.input_dim = input_dim
      self.mid_dim = midlayer_dim
      self.output_dim = output_dim

      self.model = nn.Sequential(
        nn.Linear(self.input_dim, self.mid_dim),
        nn.Linear(self.mid_dim, self.mid_dim),
        nn.Tanh(),
        # nn.Linear(self.mid_dim, self.mid_dim),
        nn.Linear(self.mid_dim, self.output_dim),
        nn.Softmax(dim=1)
      ).to(device)

      # optimizer
      self.optimizer = optim.Adam(self.model.parameters(), lr=0.01)

      # loss
      self.kl_weight = 1e-4
      self.bce_loss = nn.BCELoss().to(device)
      self.mse_loss = nn.MSELoss().to(device)
      self.kl_loss = bnn.BKLLoss(reduction='mean', last_layer_only=False).to(device)
      self.criterion = nn.CrossEntropyLoss().to(device)

    def load_model_from_file(self):
      load_successfully = False
      try:
        self.model.load_state_dict(torch.load(self.model_file))
        load_successfully = True
      except:
        pass
      return load_successfully
    
    def save_model2file(self):
      # save model
      torch.save(self.model.state_dict(), self.model_file)
      # save for c++ reading
      sript_model = torch.jit.script(self.model)
      sript_model.save(self.script_model_file)

    def get_loss(self, pred, target):
      bce = self.bce_loss(pred, target)
      loss = bce
      return loss

    def train_once(self, epoch, epoch_num,
                         input_vec, target_vec,
                         epoch2debug=20):
      target_vec = target_vec.to(self.device)

      self.optimizer.zero_grad()
      pred_vec = self.forward(input_vec)

      loss = self.get_loss(pred_vec, target_vec)
      loss.backward()
      self.optimizer.step()
      self._learning_rate_decay(epoch)

      if self.initial_loss == None:
        self.initial_loss = loss.item()

      if epoch % int(epoch2debug) == 0:
        print('\r Epoch [{}/{}], Loss: {:.4f} / Initial {:.4f};'\
              .format(epoch+1, epoch_num, loss.item(), self.initial_loss), 
              end="")

    def forward(self, input_vec):
      input_vec = input_vec.to(self.device)
      pred_vec = self.model(input_vec)
      return pred_vec

    def _learning_rate_decay(self, epoch):
      if epoch > 0 and epoch % 100 == 0:
        for p in self.optimizer.param_groups:
            p["lr"] *= 0.95
