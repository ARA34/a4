Welcome to my updated journaling Python program.

From my last journaling Python program, this one now includes the option to create and online account, change your bio on this online account,
and post to an online server.

The online server is: https://ics32distributedsocial.com/index.html

How to use:

Step 1: Prepare to run the program

    1. Open terminal and cd to the folder containing this code.
    2. Type [python3 a4.py]  -- the text inside brackets

Step 2: Running the program

    1. The program will prompt you with creating a file or loading a file choose your option.

        - If you choose to create a file, you will then be asked for a repository and filename.
        - If you choose to load a file, you will be asked for a directory to said file.


    2. Then you will be asked to publish whatever you enter next online or remain offfline (at this point you have been offline)

        - If you choose to publish information online, any profiles, posts, or change of bios, will be recorded on the server. 
        Also you will be prompted to enter a server address

        - If you choose to remain offline, you will continue on with the program without publishing anything online.


    3. Then you are prompted with the 'E' for edit or 'P' for print options.

        - If you pick 'E' these are your options:
            ("'-usr'     - Edit username.")
            ("'-pwd'     - Edit password.")
            ("'-bio'     - Edit bio.")
            ("'-addpost' - Add a post.")
            ("'-delpost' - Delete a post.")

        - If you pick 'P' these are your options:

            ("'-usr'   - Print username.")
            ("'-pwd'   - Print password.")
            ("'-bio'   - Print bio.")
            ("'-post'  - Print post based on ID.")
            ("'-posts' - Print all posts.")
            ("'-all'   - Print all information.")


API Implementation:
Include @weather in your posts to include the real time description of Irvine weather
Include @lastfm in your post to include the number of plays for kanye's top song