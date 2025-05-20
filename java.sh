#!/usr/bin/bash
 
check_directory_empty() {
    local directory=$1
    local name=$2
    if [ -z "$(ls -A $directory)" ]; then
        echo $2 "-notexists"
    else
        echo $2 "-exists"
    fi
}
rm -rf /home/coder/project/workspace/Project/screenshots
rm -rf /home/coder/project/workspace/Project/logs
rm -rf /home/coder/project/workspace/Project/reports
rm -rf /home/coder/project/log.log
touch /home/coder/project/log.log
cp /home/coder/project/workspace/selenium/EventHandler.java /home/coder/project/workspace/Project/src/test/java/utils/EventHandler.java
cd /home/coder/project/workspace/Project
mvn -q test
cp /home/coder/project/workspace/selenium/EventHandleDummy.java /home/coder/project/workspace/Project/src/test/java/utils/EventHandler.java
cat /home/coder/project/log.log
logdir="/home/coder/project/workspace/Project/logs"
scrdir="/home/coder/project/workspace/Project/screenshots"
reportsdir="/home/coder/project/workspace/Project/reports"
 
check_directory_empty $logdir "log";
check_directory_empty $scrdir "scr";
check_directory_empty $reportsdir "reports";
 
logfile=$(find /home/coder/project/workspace/Project/logs -type f -name "*.log" -print -quit)

line_count=0
 
# Check if the logfile exists
if [ -f "$logfile" ]; then
    line_count=$(wc -l < "$logfile")
    echo "Line count in log file: $line_count"  # Added line to print line_count
else
    echo "Logfile does not exist."
fi
 
# Proceed with comparison if line_count is valid
if [ "$line_count" -gt 5 ]; then
    echo "The log file with lines"
else
    echo "The log has 5 or fewer lines."
fi
 
 

# Check for "Click" in the log file
if grep -q "click on signin" "$logfile"; then
    echo "found in log file"
else
    echo "Not in log"
fi

# Check if the filename contains a year (four consecutive digits)
if [[ "$logfile" =~ [0-9]{4} ]]; then
    echo "log_timestamp"
else
    echo "no_timestamp"
fi

# Correct report file path
reportfile=$(find /home/coder/project/workspace/Project/reports -name "*.html" -print -quit)
 
 
# Check if the report file exists
if [ -f "$reportfile" ]; then
    # Uncomment the next line if you want to display the contents of the report
    # echo "Report file exists. Displaying contents:"
    # cat "$reportfile"
   
    # Count and display the number of lines in the report file
    echo "Number of lines in report:"
    line_count=$(wc -l < "$reportfile")
    echo "$line_count"
 
    # Check if the number of lines is greater than 15
    if [ "$line_count" -gt 300 ]; then
        echo "The report file with lines"
    else
        echo "The report file has 300 or fewer lines."
    fi
else
    echo "Report file does not exist."
fi
 
    # Check if "click on Blog" exists in the report
    if grep -q "hover on explore" "$reportfile"; then
        echo "found in report file"
    else
        echo "not in report"
    fi
 
s
# Find the most recent PNG file based on modification time
recent_png=$(find /home/coder/project/workspace/Project/screenshots -type f -name "*.png" -printf "%T@ %p\n" | sort -n | tail -1 | cut -d' ' -f2-)
 
if [[ -n "$recent_png" ]]; then
    echo "Most recent PNG file: $recent_png"
 
    # Get the modification timestamp of the file
    file_timestamp=$(stat -c %y "$recent_png" | cut -d'.' -f1)
    echo "File timestamp: $file_timestamp"
else
    echo "No PNG file found in the screenshot folder."
fi



#log withtimestamp
recent_log=$(find /home/coder/project/workspace/Project/logs -type f -name "*.log" -print -quit)


if [[ -n "$recent_log" ]]; then

      # Extract timestamps with milliseconds and find the latest one
    # Assuming the timestamp format is: YYYY-MM-DD HH:MM:SS,SSS
    recent_timestamp=$(grep -oP '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}' "$recent_log" | sort | tail -1)

    if [[ -n "$recent_timestamp" ]]; then
        echo "Most recent log entry"
    else
        echo "No valid log"
    fi
else
    echo "No .log file found in the directory."
fi

# Find the first HTML report file with scr in the reports directory
reportfile=$(find /home/coder/project/workspace/Project/reports -name "*.html" -print -quit)

# Check if the report file was found
if [[ -n "$reportfile" ]]; then
    # Search for any .png image file that contains "destination_guide" in its name
    if grep -qE 'src="[^"]*agronetto_screenshot[^"]*\.png"' "$reportfile"; then
        echo "png is found in the report file"
    else
        echo "No image in report"
    fi
else
    echo "No report"
fi


