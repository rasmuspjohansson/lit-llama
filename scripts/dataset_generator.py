# simple script showing how to generate a dataset programatically
# on how to train on the dataset see: https://github.com/Lightning-AI/lit-llama/blob/main/howto/finetune_adapter_v2.md#tune-on-your-dataset

import json
import random
list=[]
for i in range(100000):
        numbers = [random.randint(0,1000) for j in range(10)]
        list.append( {
        "instruction": "Arrange the given numbers in ascending order.",
        "input": str(numbers),
        "output": str(sorted(numbers))
    })
out_file = open("debugset.json", "w")
  
json.dump(list, out_file, indent = 6)
  
out_file.close()


