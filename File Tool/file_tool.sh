#!/bin/bash

echo "Choise one option: 1. TO create folder  2. To Delete folder 3. exit"
read options
dt=$(date '+%d/%m/%Y %H:%M:%S');

function create_folder() {
    echo "Folder name $folder"
    mkdir $folder
    touch $folder/main.py
    echo "#$dt" >> $folder/main.py
    touch $folder/README.md
    echo "#$dt" >> $folder/README.md
    touch $folder/notes.txt
    echo "#$dt" >> $folder/notes.txt
    mv $folder/notes.txt $folder/log.txt
    echo "$folder created successfully!"

}

function delete_folder(){
    echo "Folder to be Deleted $folder"
    rm -r $folder
    echo "Folder $folder Deleted"
}

case $options in
    "1")
        echo "Folder to be created enter the name"
        read folder
        create_folder "$folder"
        ;;
    "2")
        echo "Folder to be deleted"
        read folder
        delete_folder "$folder"
        ;;
    *)
        echo "Done"
        ;;
esac
