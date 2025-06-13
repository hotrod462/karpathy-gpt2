import csv

input_csv = "pewdiepie.csv"
output_txt = "pewdiepie_transcripts.txt"
transcript_column = "transcript"  # Change this if your column has a different name

with open(input_csv, "r", encoding="utf-8") as csvfile, open(output_txt, "w", encoding="utf-8") as txtfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        transcript = row.get(transcript_column, "")
        if transcript:
            txtfile.write(transcript.strip() + "\n")

print(f"Transcripts extracted to {output_txt}")
