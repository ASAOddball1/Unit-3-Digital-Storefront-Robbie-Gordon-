def Credit():
    import tkinter as tk
    import webbrowser
    from PIL import Image, ImageTk

    # Function to open a URL in the default web browser
    def open_url(url):
        webbrowser.open(url)

    def display_information(name, avatar_path, introduction, hobbies, goals, media_links):
        info_window = tk.Toplevel(root)
        info_window.title(f"{name}'s Digital Representation")

        # Name
        name_label = tk.Label(info_window, text=f"Name: {name}")
        name_label.pack()

        # Avatar (display an image)
        avatar_image = Image.open(avatar_path)
        avatar_photo = ImageTk.PhotoImage(avatar_image)
        avatar_label = tk.Label(info_window, image=avatar_photo)
        avatar_label.image = avatar_photo  # To prevent the image from being garbage collected
        avatar_label.pack()

        # Introduction
        introduction_label = tk.Label(info_window, text=f"Introduction: {introduction}")
        introduction_label.pack()

        # Hobbies
        hobbies_label = tk.Label(info_window, text=f"Hobbies: {', '.join(hobbies)}")
        hobbies_label.pack()

        # Future Goals
        goals_label = tk.Label(info_window, text=f"Future Goals: {', '.join(goals)}")
        goals_label.pack()

        # Favorite Media
        media_label = tk.Label(info_window, text="Favorite Media:")
        media_label.pack()

        # Create buttons for media links
        for media_name, media_link in media_links.items():
            media_button = tk.Button(info_window, text=media_name, command=lambda link=media_link: open_url(link))
            media_button.pack()

    root = tk.Tk()
    root.title("Digital Representation")

    # Set the name to "Robbie Gordon"
    example_name = "Robbie Gordon"
    # Set the path to the avatar image file
    example_avatar = 'channels4_profile.jpg'

    example_introduction = "I am from Surrey BC, and I love Playing Instruments."
    example_hobbies = ["I play the guitar, drums and piano ", "Playing And Making Video Games"]
    example_goals = ["To Be Able To Model Objects In Blender Well", "To Produce And Make Video Games As a Job"]
    # Create a dictionary of media names and their corresponding URLs
    example_media_links = {
        "YouTube": "https:/www.youtube.com/@Oddball12",
        "TikTok": "https://www.tiktok.com/@asa_oddball",
        "Facebook": "https://www.facebook.com/Oddballishere",
        "Instagram": "https://www.instagram.com/oddballishere/"

    }

    # Create a button to display Robbie Gordon's information
    robbie_info_button = tk.Button(root, text=f"{example_name}'s Info", command=lambda: display_information(
        example_name, example_avatar, example_introduction, example_hobbies, example_goals, example_media_links))
    robbie_info_button.pack()

    root.mainloop()





