
# Reading in puzzle input
f = open("inputs/input.txt", "r")
data = f.readlines()
f.close()

elf_idx = 0
elf_calories = [0]
second_elf = None
third_elf = None
max_elf = 0
update_standing = False

for idx in range(len(data)):
   # Remove new line characters
   line = data[idx].rstrip("\n")

   if (idx == len(data) - 1 or \
      len(data[idx + 1].rstrip("\n")) == 0):
      update_standing = True

   
   if (len(line) == 0):
      # New Elf
      elf_idx += 1
      elf_calories.append(0)
   else:
      # Update Elf calories
      elf_calories[elf_idx] += int(line)

   
   if update_standing:
      # Update 1st elf
      temp = None
      if (max_elf != elf_idx and elf_calories[elf_idx] > elf_calories[max_elf]):
         temp = max_elf
         max_elf = elf_idx

      # Update 2nd Elf
      temp2 = None
      if (temp is not None):
         # If 1st elf has been updated
         temp2 = second_elf
         second_elf = temp
      elif (max_elf != elf_idx and \
         (second_elf is None or \
            elf_calories[elf_idx] > elf_calories[second_elf])):
         # If you need to update ONLY second elf
         temp2 = second_elf
         second_elf = elf_idx

      # Update 3rd elf
      if (temp2 is not None):
         # If 2nd elf has been updated
         third_elf = temp2
      elif (max_elf != elf_idx and second_elf != elf_idx and \
         (third_elf is None or  \
         elf_calories[elf_idx] > elf_calories[third_elf])):
         # If you need to updated ONLY third elf
         third_elf = elf_idx
      
      update_standing = False


   print(f"{elf_idx} {elf_calories[elf_idx]} {max_elf}, {second_elf}, {third_elf}")

print(elf_calories)

print(f"1st Elf: {max_elf + 1}, Calories: {elf_calories[max_elf]}")
print(f"2nd Elf: {second_elf + 1}, Calories: {elf_calories[second_elf]}")
print(f"3rd Elf: {third_elf + 1}, Calories: {elf_calories[third_elf]}")
print(f"Total Calories: {elf_calories[max_elf] + elf_calories[second_elf] + elf_calories[third_elf]}")



