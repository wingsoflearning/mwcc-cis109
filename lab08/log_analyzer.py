# -------------------------------------------------------------
# LAB 8: Log File Analyzer
# -------------------------------------------------------------

#STEP 1: Read the input file
# Open application.log and process its entries one at a time.

# with open('application.log', 'r') as file:
#     content = file.read()
#     print(content)

# -------------------------------------------------------------
#STEP 2: Extract timestamps using slicing
# Extract the timestamp from the beginning of each log entry (first 19 characters).

# with open('application.log', 'r') as file:
#     for line in file:
#         timestamp = line[:19]
#         print(timestamp)

# -------------------------------------------------------------
#STEP 3: Search log entries
# Use the in operator and find() method to identify error and warning entries.

# with open('application.log', 'r') as file:
#     for line in file:
#         #convert line to lowercase to catch inconsistent capitalization
#         lower_line = line.lower()
#         #in operator to look for error, use find to look for warning, -1 for false return of anything else
#         if "error" in lower_line or lower_line.find("warning") != -1:
#             print(line.strip())

# -------------------------------------------------------------
#STEP 4: Standardize severity labels
# Use replace() to convert lowercase occurrences of error and warning to uppercase.
# Your report must consistently use ERROR and WARNING.

# with open('application.log', 'r') as file:
#     for line in file:
#         # Standardize the lowercase labels to uppercase using replace()
#         standardized_line = line.replace("error", "ERROR").replace("warning", "WARNING")
#         fields = standardized_line.split("|")
#         print(standardized_line.strip())

# -------------------------------------------------------------
#STEP 5: Split entries into fields
# Use split() with the pipe character (|) to separate fields and remove whitespace.

# with open('application.log', 'r') as file:
#     for line in file:
#         #standardize labels
#         standardized_line = line.replace("error", "ERROR").replace("warning", "WARNING")
#         #split by the pipe into a list
#         fields = standardized_line.split("|")
#         #index and strip extra spacing
#         timestamp = fields[0].strip()
#         severity = fields[1].strip()
#         message = fields[2].strip()
#         #removed | and put it in print statement so looks the same but tested without | in print statement and it was removed
#         print(f"{timestamp} | {severity} | {message}")

# -------------------------------------------------------------
#STEP 6: Filter the entries
# Include only entries whose severity is ERROR or WARNING.

# with open('application.log', 'r') as file:
#     for line in file:
#         #standardize labels
#         standardized_line = line.replace("error", "ERROR").replace("warning", "WARNING")
#         #split by the pipe into a list
#         fields = standardized_line.split("|")
#         #index and strip extra spacing
#         timestamp = fields[0].strip()
#         severity = fields[1].strip()
#         message = fields[2].strip()
#         #only print if the severity is ERROR or WARNING
#         if severity =="ERROR" or severity =="WARNING":
#             print(f"{timestamp} | {severity} | {message}")

# -------------------------------------------------------------
#STEP 7: Format the report
# Use join() to combine the cleaned fields with - as the separator.

# with open('application.log', 'r') as file:
#     for line in file:
#         #standardize labels
#         standardized_line = line.replace("error", "ERROR").replace("warning", "WARNING")
#         #split by the pipe into a list
#         fields = standardized_line.split("|")
#         #index and strip extra spacing
#         timestamp = fields[0].strip()
#         severity = fields[1].strip()
#         message = fields[2].strip()
#         #only print if the severity is ERROR or WARNING
#         if severity =="ERROR" or severity =="WARNING":
#             #combine thdivvidual fields into a single list
#             log_list = [timestamp, severity, message]
#             #use join to combine them with "-"
#             formatted_line = "-".join(log_list)
#             print(formatted_line)

# -------------------------------------------------------------
#STEP 8: Display a summary
# At the end of the report, display the total number of errors and warnings included.

#initialize counter to start
# count = 0
# #print report headers
# print("ERROR REPORT")
# print("-" * 40)

# with open('application.log', 'r') as file:
#     for line in file:
#         #standardize labels
#         standardized_line = line.replace("error", "ERROR").replace("warning", "WARNING")
#         #split by the pipe into a list
#         fields = standardized_line.split("|")
#         #index and strip extra spacing
#         timestamp = fields[0].strip()
#         severity = fields[1].strip()
#         message = fields[2].strip()
#         #only print if the severity is ERROR or WARNING
#         if severity =="ERROR" or severity =="WARNING":
#             #combine idividual fields into a single list
#             log_list = [timestamp, severity, message]
#             #use join to combine them with "-"
#             formatted_line = "-".join(log_list)
#             print(formatted_line)

#             #ongoing counter for each error or warning
#             count += 1

# #print the summary count at the very end
# print()
# print(f"Total errors and warnings: {count}")

# -------------------------------------------------------------
#STEP 9: Use appropriate comments
# (Handled throughout the major sections above)

#initialize counter to start
count = 0
#print report headers
print("ERROR REPORT")
print("-" * 40)

# --- STEP 1: Open the Input File ---
with open('application.log', 'r') as file:
    for line in file:
        # --- STEP 4: Standardize Severity Labels ---
        #standardize labels lowercase to uppercase
        standardized_line = line.replace("error", "ERROR").replace("warning", "WARNING")
        
        # --- STEP 5: Split Entries into Fields ---
        #split by the pipe into a list
        fields = standardized_line.split("|")
        
        #index and strip extra spacing
        timestamp = fields[0].strip()
        severity = fields[1].strip()
        message = fields[2].strip()
        
        # --- STEP 6: Filter the Entries ---
        #only print if the severity is ERROR or WARNING
        if severity == "ERROR" or severity == "WARNING":
            # --- STEP 7: Format the Report String ---
            #combine individual fields into a single list
            log_list = [timestamp, severity, message]
            #use join to combine them with "-"
            formatted_line = " - ".join(log_list)
            print(formatted_line)
            
            #ongoing counter for each error or warning
            count += 1

# --- STEP 8: Display Final Summary Count ---
#print the summary count at the very end
print()
print(f"Total errors and warnings: {count}")