"""

task: https://eacp.energyaustralia.com.au/codingtest
data: 21/09/2022
Author: Della Li

"""

import pdb

sample_list = [
  {
    "name": "LOL-palooza",
    "bands": [
      {
        "name": "Frank Jupiter",
        "recordLabel": "Pacific Records"
      },
      {
        "name": "Jill Black",
        "recordLabel": "Fourth Woman Records"
      },
      {
        "name": "Werewolf Weekday",
        "recordLabel": "XS Recordings"
      },
      {
        "name": "Winter Primates",
        "recordLabel": ""
      }
    ]
  },
  {
    "bands": [
      {
        "name": "Critter Girls",
        "recordLabel": "ACR"
      },
      {
        "name": "Propeller",
        "recordLabel": "Pacific Records"
      }
    ]
  },
  {
    "name": "Trainerella",
    "bands": [
      {
        "name": "YOUKRANE",
        "recordLabel": "Anti Records"
      },
      {
        "name": "Manish Ditch",
        "recordLabel": "ACR"
      },
      {
        "name": "Adrian Venti",
        "recordLabel": "Monocracy Records"
      },
      {
        "name": "Wild Antelope",
        "recordLabel": "Still Bottom Records"
      }
    ]
  },
  {
    "name": "Small Night In",
    "bands": [
      {
        "name": "Wild Antelope",
        "recordLabel": "Marner Sis. Recording"
      },
      {
        "name": "Jill Black",
        "recordLabel": "Fourth Woman Records"
      },
      {
        "name": "The Black Dashes",
        "recordLabel": "Fourth Woman Records"
      },
      {
        "name": "Yanke East",
        "recordLabel": "MEDIOCRE Music"
      },
      {
        "name": "Green Mild Cold Capsicum",
        "recordLabel": "Marner Sis. Recording"
      },
      {
        "name": "Squint-281",
        "recordLabel": "Outerscope"
      }
    ]
  },
  {
    "name": "Twisted Tour",
    "bands": [
      {
        "name": "Summon",
        "recordLabel": "Outerscope"
      },
      {
        "name": "Auditones",
        "recordLabel": "Marner Sis. Recording"
      },
      {
        "name": "Squint-281"
      }
    ]
  }
]

def get_data_from_api():
  """get_data_from_api"""

#
def parser():
  """parser"""
  # {company:{band1:[], band2:[]}}
  record = {}

  for item_dict in sample_list:
      # print('=====>', item_dict)
      # print(type(item_dict))
      # print(item_dict.keys())
      festival = item_dict.get('name', '')
      # print('festival:', festival)
      for sub_item in item_dict['bands']:
          company = ''
          band = ''
          company = sub_item.get('recordLabel', '')
          # print('company:', company)
          band = sub_item['name']
          if company not in record:
              record[company] = {}
              record[company][band] = [festival]
          else:
              if band not in record[company]:
                  record[company][band] = [festival]
              else:
                  if festival not in record[company][band]:
                      record[company][band].append(festival)

  print(record)

if __name__ == '__main__':
  parser()
