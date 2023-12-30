
![Logo](https://raw.githubusercontent.com/daemonexe/daemonexe/main/TEMPLATE.png)


# Password Manager v3.2.3
Introducing Password Manager, a user-friendly password manager coded with Python, dedicated to preserving users privacy and enhancing security. Unlike conventional password managers, Password Manager steers clear of cloud connections ensuring that your sensitive data stays securely on your personal computer with encrpytion. You can effortlessly import and export your encrypted password files as needed, providing flexibility without compromising on security. 

What sets Password Manager apart is its built-in password generator, simplifying the process of creating strong and unique passwords. With Password Manager, you maintain full control over your data, offering a reliable and user-centric solution for securely managing your passwords on your local machine.

Lets take back control!!

## Screenshots
## 1 Log in interface
It's very obvious just create admin username and password; you don't want people snooping your passwords when you are away 
![App Screenshot](https://github.com/daemonexe/daemonexe/blob/main/Screenshot%202023-01-17%20133252.png?raw=true)
## 
## 2 Main interface
This interface displays all of your passwords
![App Screenshot](https://github.com/daemonexe/daemonexe/blob/main/Screenshot%202023-01-17%20133138.png?raw=true)
### 
## Installation
It's very straightforward just download the zip file form assets > extract it > run installer.exe....


# Modules used 
| module | function used     | Description                       |
| :-------- | :------- | :-------------------------------- |
| tkinter      | `*` | to create a GUI for the application |
| sqlite      | `*` | to manage database files  |
| os      | `os.remove()` | to remove the database file |
| string      | `string.uppercase()` | to generate text for passwords  |
| messagebox      | `messagebox.showinfo()` | to create pop up windows |

## Features

- Passwords are encrypted 
- passwords and be saved and imported 
- search indexing for passwords (easy to find)
- includes a password generator 
- copy/paste buttons 
- Dark Mode UI with animations 

## Optimizations

The project included many optimizations, including storing passwords in a database file and reducing the image file size, as well as a slightly optimized password generator.

## FAQ

#### Q1 : Will the passwords ever be compromised?

A1 : The program is open source the passwords are stored in your drive.

#### Q2 : What is the database used in this program

A2 : Its MySqlite, a light version of SQL


## Installation

Got to the latest releases and then dowload the zip file [latest_release](https://github.com/daemonexe/password-Manager/releases/tag/v3.2.3)
- unzip it and run the installer.exe
- It's a installer.exe file jusst dowload it and click next, next....







## Bugs:
- Minor bug if the file name is renamed while importing/exporting it fails to do the action due to some permission limitations 


## Authors

- [@daemonexe](https://github.com/daemonexe)

