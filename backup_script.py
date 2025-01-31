import os
import zipfile
from datetime import datetime

def backup_folder(source_folder, backup_location):
    # বর্তমান তারিখের সাথে ব্যাকআপ ফাইলের নাম তৈরি
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # 'S' সঠিক ফরম্যাট
    backup_filename = f"backup_{date_str}.zip"
    backup_path = os.path.join(backup_location, backup_filename)
    
    try:
        # ফোল্ডারটি জিপ আর্কাইভে কম্প্রেস করা
        with zipfile.ZipFile(backup_path, "w", zipfile.ZIP_DEFLATED) as backup_zip:
            for root, dirs, files in os.walk(source_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    backup_zip.write(file_path, os.path.relpath(file_path, source_folder))
        
        print(f"ব্যাকআপ সফল! ফাইলটি সংরক্ষিত হয়েছে: {backup_path}")
    
    except Exception as e:
        print(f"ব্যাকআপ করতে গিয়ে ত্রুটি ঘটেছে: {e}")

# ব্যবহারকারীর কাছ থেকে ইনপুট নেয়া
source_folder = input("Enter the path to the folder you want to backup.: ")  # ব্যাকআপ নিতে চাওয়া ফোল্ডার
backup_location = input("Enter the destination path to save the backup file.: ")  # যেখানে ব্যাকআপ সংরক্ষণ হবে

# ফাংশন কল করা
backup_folder(source_folder, backup_location)