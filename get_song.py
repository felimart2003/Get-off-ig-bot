def clean_metadata(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    with open(file_path, "w") as f:
        for line in lines:
            if line.strip("\n") != "Searching for music...":
                line = (
                    line.replace("[Track(id=", "Track(\n\tid=")
                    .replace(", ", ",\n\t")
                    .replace("Url(", "")
                    .replace(")", "")
                    .replace(
                        "territory_validity_periods={}", "territory_validity_periods={}\n\t)"
                    )
                )
                f.write(line)

def main():
  print("Cleaning...")
  file_path = "./songs_data.txt"
  clean_metadata(file_path)
  # print(clean_metadata)
  print("Cleaned music metadata!")

if __name__ == "__main__":
  main()
