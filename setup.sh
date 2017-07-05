#!/bin/sh

sudo apt-get update
sudo apt-get install vim python3 python3-pip olsrd git -y
{
echo 'syntax on'
echo 'set autoindent'
echo 'set expandtab'
echo 'set tabstop=4'
echo 'set shiftwidth=4'
echo 'set cursorline'
echo 'set number'
} > ~/.vimrc

sudo pip3 install Flask
sudo pip3 install netifaces
