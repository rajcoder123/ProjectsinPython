"""Code To Display the Profile Picture of Instagram"""
import instaloader
ig=instaloader.Instaloader()
profile="Enter Username Here"
ig.download_profile(profile,profile_pic_only=True)
