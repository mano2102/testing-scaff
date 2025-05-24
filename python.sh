#!/usr/bin/bash

check_directory_empty() {
    local directory=$1
    local name=$2
    if [ -z "$(ls -A $directory 2>/dev/null)" ]; then
        echo "$name -notexists"
    else
        echo "$name -exists"
    fi
}

# Define paths
base_dir="/home/coder/project/workspace/Project"
logdir="$base_dir/logs"
scrdir="$base_dir/screenshot"
reportsdir="$base_dir/Report/AllureReports"

# Cleanup old data
rm -rf "$scrdir"
rm -rf "$logdir"
rm -rf "$reportsdir"
rm -rf /home/coder/project/workspace/Project/Report/AllureReports/AllureReports_*
rm -f /home/coder/project/log.log
touch /home/coder/project/log.log

# Copy eventhandler file and run Python script
cp "$base_dir/selenium/eventhandler.py" "$base_dir/utilities/eventhandler.py"
cd "$base_dir" || exit
python3 base.py

# Replace eventhandler with dummy after run
cp "$base_dir/selenium/eventhandlerdummy.py" "$base_dir/utilities/eventhandler.py"

# Show log file content
cat /home/coder/project/log.log

# Check directories if empty or not
check_directory_empty "$logdir" "log"
check_directory_empty "$scrdir" "scr"
check_directory_empty "$reportsdir" "report"

# Find a log file
logfile=$(find "$logdir" -type f -name "*.log" -print -quit)
line_count=0

if [ -f "$logfile" ]; then
    line_count=$(wc -l < "$logfile")
    echo "Line count in log file: $line_count"
else
    echo "Logfile does not exist."
fi

if [ "$line_count" -gt 5 ]; then
    echo "The log file has more than 5 lines"
else
    echo "The log has 5 or fewer lines."
fi

# Search for specific log content
if [ -f "$logfile" ] && grep -q "Clicked Submit" "$logfile"; then
    echo "Found 'Clicked Submit' in log file"
else
    echo "Not found in log"
fi

# Check if log filename contains a year (four digits)
if [[ "$logfile" =~ [0-9]{4} ]]; then
    echo "log_timestamp"
else
    echo "no_timestamp"
fi

# Find report HTML file in AllureReports
reportfile=$(find "$reportsdir" -name "*.html" -print -quit)

if [ -f "$reportfile" ]; then
    echo "Allure report file found: $reportfile"
    line_count=$(wc -l < "$reportfile")
    echo "Number of lines in report: $line_count"
    if [ "$line_count" -gt 300 ]; then
        echo "The report file has more than 300 lines."
    else
        echo "The report file has 300 or fewer lines."
    fi
    if grep -q "hover on explore" "$reportfile"; then
        echo "Found keyword 'hover on explore' in report file"
    else
        echo "Keyword not found in report file"
    fi
else
    echo "Report file does not exist."
fi

# Find the most recent PNG screenshot
recent_png=$(find "$scrdir" -type f -name "*.png" -printf "%T@ %p\n" | sort -n | tail -1 | cut -d' ' -f2-)

if [[ -n "$recent_png" ]]; then
    echo "Most recent PNG file: $recent_png"
    file_timestamp=$(stat -c %y "$recent_png" | cut -d'.' -f1)
    echo "File timestamp: $file_timestamp"
else
    echo "No PNG file found in the screenshot folder."
fi

# Find most recent log entry timestamp with milliseconds
recent_log=$(find "$logdir" -type f -name "*.log" -print -quit)

if [[ -n "$recent_log" ]]; then
    recent_timestamp=$(grep -oP '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}' "$recent_log" | sort | tail -1)
    if [[ -n "$recent_timestamp" ]]; then
        echo "Most recent log entry timestamp: $recent_timestamp"
    else
        echo "No valid log timestamp found"
    fi
else
    echo "No .log file found in the directory."
fi

# Check for specific PNG image reference in Allure report
if [[ -f "$reportfile" ]]; then
    if grep -qE 'src="[^"]*list[^"]*\.png"' "$reportfile"; then
        echo "PNG image found in report file"
    else
        echo "No image found in report file"
    fi
else
    echo "No report file to check for images"
fi
