#!/usr/bin/env python

import pickle

def write_dict2bin(dict_data, file):
  f = open(file, 'wb')
  pickle.dump(dict_data, f)
  f.close()
  print("file writed at %s" %(file))

def read_dict_from_bin(file):
  f = open(file, 'rb')
  get_dict = pickle.load(f)
  print("file readed given %s" %(file))
  return get_dict

