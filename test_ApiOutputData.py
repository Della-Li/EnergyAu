"""

task: https://eacp.energyaustralia.com.au/codingtest/testers
Option: Integration QE role
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

noneFestival = 0
noneRecordLabel = 0
noneBandName = 0

def get_data_from_api():
  """get_data_from_api"""

#
def parse_apiOutputData():

  noneFestival = 0
  noneRecordLabel = 0
  noneBandName = 0

  for item_dict in sample_list:

      festival = item_dict.get('name')
      # print('festival:', festival)
      if festival == None:
        noneFestival += 1

      for sub_item in item_dict['bands']:

        # print("sub_item", sub_item)
        bandName = sub_item.get('name')
        # print("bandName: ", bandName)
        if bandName == None:
          noneBandName += 1

        lable = sub_item.get('recordLabel')
        if lable == None:
          noneRecordLabel += 1

  return noneFestival, noneBandName, noneRecordLabel


def test_festival(noneFestival):
  #assert noneFestival == 0
  if noneFestival:
    print("MusicFestival have None value")
  else:
    print("MusicFestival pass!")


def test_bandname(noneBandName):
  #assert noneBandName == 0
  if noneBandName:
    print("BandName have None value")
  else:
    print("BandName pass!")

def test_recordlabel(noneRecordLabel):
  #assert noneRecordLabel == 0
  if noneRecordLabel:
    print("RecordLabel have None value")
  else:
    print("RecordLabel pass!")

noneFestival, noneBandName, noneRecordLabel = parse_apiOutputData()

# print("noneFestival :", noneFestival)
# print("noneBandName :", noneBandName)
# print("noneRecordLabel :", noneRecordLabel)

test_festival(noneFestival)
test_bandname(noneBandName)
test_recordlabel(noneRecordLabel)