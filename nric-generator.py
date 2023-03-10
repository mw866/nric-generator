#!/usr/local/bin/python
import argparse, random

def get_identification_no(identification):
  weight = (2,7,6,5,4,3,2) 
  alpha_singaporean = ('J','Z','I','H','G','F','E','D','C','B','A')
  alpha_foreigner= ('X','W','U','T','R','Q','P','N','M','L','K')
  
  total_sum = 0
  for i in range (len(weight)):
    current_product = weight[i] * int(identification[i+1])
    total_sum += current_product
  
  #if 'T' or 'G' total_sum plus 4
  if (identification[0] in ('T','G')) :
    total_sum += 4
  
  #if 'M' total_sum plus 3
  if (identification[0] in ('M')) :
    total_sum += 3

  remainder = total_sum % 11
    
  # generate the last checksum letter
  if (identification[0] in ('S', 'T')):
    return identification+alpha_singaporean[remainder]
  elif(identification[0] in ('F', 'G', 'M')):
    return identification+alpha_foreigner[remainder]

def main():
  parser = argparse.ArgumentParser(description="Singapore NRIC and FIN number generation tool")
  parser.add_argument('--prefixes',  '-p', nargs="+", default=['S', 'T', 'F', 'G', 'M'], help='The prefixes of NRIC / FIN to be generated. S/T for NRIC. F/G/M for FIN')
  parser.add_argument('--min', type=int, default=0, choices=range(0, 100), help='The MIN first two digits representing year of birth')
  parser.add_argument('--max', type=int, default=99, choices=range(0, 100), help='The MAX first two digits representing year of birth')
  parser.add_argument('--num', '-n', type=int, default=99, help='Number of NRIC / FIN numbers to generate')
  args = vars(parser.parse_args())
  # print(args)
  generate(args["prefixes"], args["min"], args["max"], args["num"])

def generate(prefixes, min, max, num):
  prefixes = [prefix.upper() for prefix in prefixes]

  for i in range(num):
    prefix=random.choice(prefixes)
    year=f"{random.choice(range(min, max+1)):02}"
    identification = prefix + year +'{0:05}'.format(i)
    print(get_identification_no(identification))

if __name__ == "__main__":
    main()