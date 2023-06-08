import tkinter
import tkinter.messagebox
from tkinter import filedialog
import customtkinter
from PIL import ImageTk, Image, ImageOps , ImageEnhance, ImageFilter



customtkinter.set_appearance_mode("Dark")  
customtkinter.set_default_color_theme("green")  

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("PixAlchemy 1.0")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # Logo
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="PixAlchemy 1.0", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 0))

        self.name_label = customtkinter.CTkLabel(self.sidebar_frame, text="Oleh: Reswara Argya Munda\nUpdate Terakhir: 08/06/2023", font=customtkinter.CTkFont(size=10, weight="normal"))
        self.name_label.grid(row=1, column=0, padx=20, pady=(0, 10))

        #sidebar
        #Appearance
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=2, column=0, padx=20, pady=(10, 5))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=3, column=0, padx=20, pady=(0, 0))

        
        #image
        self.main_image = Image.open("boat.jpg")
        self.my_image = customtkinter.CTkImage(light_image=self.main_image,
                                  dark_image=self.main_image,
                                  size=(600, 600))
        self.image_label = customtkinter.CTkLabel(self, image=self.my_image, text="")
        self.image_label.grid(row=0, column=1, padx=(15, 5), pady=(20, 10), sticky="nsew")
        self.enhanced_image = self.main_image.copy()
        self.temp_image = self.enhanced_image


        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=1, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.tabview.add("Action")
        self.tabview.add("Tools")
        
        self.tabview.tab("Action").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Tools").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
    
        #Action Tab Menu
        self.change_image = customtkinter.CTkButton(self.tabview.tab("Action"), text="Change Image",
                                                           command=self.open_image)
        self.change_image.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.reset_image = customtkinter.CTkButton(self.tabview.tab("Action"), text="Reset Image",
                                                           command=self.reset_image)
        self.reset_image.grid(row=1, column=1, padx=20, pady=(10, 10))

        self.save_image = customtkinter.CTkButton(self.tabview.tab("Action"), text="Save Image",
                                                           command=self.save_image)
        self.save_image.grid(row=1, column=2, padx=20, pady=(10, 10))


        #Tools Menu
        self.detect_faces_button = customtkinter.CTkButton(self.tabview.tab("Tools"), text="Detect Faces"
                                                           )
        self.detect_faces_button.grid(row=1, column=0, padx=20, pady=(10, 10))


        self.edit_image = customtkinter.CTkTabview(self, width=500)
        self.edit_image.grid(row=0, column=3, padx=(10, 20), pady=(20, 20), sticky="nsew")
        self.edit_image.add("Light")
        self.edit_image.add("Filters")
 
        self.edit_image.tab("Light").grid_columnconfigure(0, weight=1)  
        
        #BRIGHTNESS
        self.brightness_label = customtkinter.CTkLabel(self.edit_image.tab("Light"), text="Brightness", anchor="w")
        self.brightness_label.grid(row=1, column=0, padx=(20, 10), pady=(10, 5), sticky="ew")
        self.brightness_slider = customtkinter.CTkSlider(self.edit_image.tab("Light"), command=self.image_manipulation, from_=0, to=2.0, number_of_steps=100)
        self.brightness_slider.grid(row=2, column=0, padx=(20, 10), pady=(5, 10), sticky="ew")

        #SHARPNESS
        self.sharpness_label = customtkinter.CTkLabel(self.edit_image.tab("Light"), text="Sharpness", anchor="w")
        self.sharpness_label.grid(row=3, column=0, padx=(20, 10), pady=(10, 5), sticky="ew")
        self.sharpness_slider = customtkinter.CTkSlider(self.edit_image.tab("Light"), command=self.image_manipulation, from_=0, to=2.0, number_of_steps=100)
        self.sharpness_slider.grid(row=4, column=0, padx=(20, 10), pady=(5, 10), sticky="ew")

        #CONTRAST
        self.contrast_label = customtkinter.CTkLabel(self.edit_image.tab("Light"), text="Contrast", anchor="w")
        self.contrast_label.grid(row=5, column=0, padx=(20, 10), pady=(10, 5), sticky="ew")
        self.contrast_slider = customtkinter.CTkSlider(self.edit_image.tab("Light"), command=self.image_manipulation, from_=0, to=2.0, number_of_steps=100)
        self.contrast_slider.grid(row=6, column=0, padx=(20, 10), pady=(5, 10), sticky="ew")
 
        #BLUR
        self.blur_label = customtkinter.CTkLabel(self.edit_image.tab("Light"), text="Blur", anchor="w")
        self.blur_label.grid(row=7, column=0, padx=(20, 10), pady=(10, 5), sticky="ew")
        self.blur_slider = customtkinter.CTkSlider(self.edit_image.tab("Light"), command=self.image_manipulation, from_=-20, to=20, number_of_steps=100)
        self.blur_slider.grid(row=8, column=0, padx=(20, 10), pady=(5, 10), sticky="ew")

        #COLOR
        self.color_label = customtkinter.CTkLabel(self.edit_image.tab("Light"), text="Color", anchor="w")
        self.color_label.grid(row=9, column=0, padx=(20, 10), pady=(10, 5), sticky="ew")
        self.color_slider = customtkinter.CTkSlider(self.edit_image.tab("Light"), command=self.image_manipulation, from_=0, to=2.0, number_of_steps=1000)
        self.color_slider.grid(row=10, column=0, padx=(20, 10), pady=(5, 10), sticky="ew")

       # self.warm_contrast_switch = customtkinter.CTkSwitch(master=self.edit_image.tab("Filter"), text="Warm Contrast", onvalue="on", offvalue="off")
       # self.warm_contrast_switch.grid(row=1, column=0, padx=(20, 10), pady=(10, 5), sticky="ew")

        # FILTERS
        self.toggle_switch = "off"

        #posterize
        self.posterize_switch_var = customtkinter.StringVar(value=self.toggle_switch)

        self.posterize_thumbnail = customtkinter.CTkImage(light_image=ImageOps.posterize(Image.open("boat_small.jpg"), 2),
                                  dark_image=ImageOps.posterize(Image.open("boat_small.jpg"), 2),
                                  size=(100, 100))
        self.posterize_thumbnail_label = customtkinter.CTkLabel(self.edit_image.tab("Filters"), image=self.posterize_thumbnail, text="")
        self.posterize_thumbnail_label.grid(row=0, column=1, padx=(15, 60), pady=(25, 0), sticky="nsew")

        self.posterize_switch = customtkinter.CTkSwitch(self.edit_image.tab("Filters"), text="posterize", 
                                                      font=customtkinter.CTkFont(size=13, weight="bold"), command=self.image_filters_posterize, variable=self.posterize_switch_var, onvalue="on", offvalue="off")
        self.posterize_switch.grid(row=2, column=1, padx=(20, 5), pady=(10, 50), sticky="nsew")

        

        #GRAYSCALE
        self.grayscale_switch_var = customtkinter.StringVar(value=self.toggle_switch)

        self.grayscale_thumbnail = customtkinter.CTkImage(light_image=ImageOps.grayscale(Image.open("boat_small.jpg")),
                                  dark_image=ImageOps.grayscale(Image.open("boat_small.jpg")),
                                  size=(100, 100))
        self.grayscale_thumbnail_label = customtkinter.CTkLabel(self.edit_image.tab("Filters"), image=self.grayscale_thumbnail, text="")
        self.grayscale_thumbnail_label.grid(row=0, column=2, padx=(15, 60), pady=(25, 0), sticky="nsew")

        self.grayscale_switch = customtkinter.CTkSwitch(self.edit_image.tab("Filters"), text="grayscale", 
                                                      font=customtkinter.CTkFont(size=13, weight="bold"), command=self.image_filters_grayscale, variable=self.grayscale_switch_var, onvalue="on", offvalue="off")
        self.grayscale_switch.grid(row=2, column=2, padx=(20, 5), pady=(10, 50), sticky="nsew")


        #INVERT
        self.invert_switch_var = customtkinter.StringVar(value=self.toggle_switch)

        self.invert_thumbnail = customtkinter.CTkImage(light_image=ImageOps.invert(Image.open("boat_small.jpg")),
                                  dark_image=ImageOps.invert(Image.open("boat_small.jpg")),
                                  size=(100, 100))
        self.invert_thumbnail_label = customtkinter.CTkLabel(self.edit_image.tab("Filters"), image=self.invert_thumbnail, text="")
        self.invert_thumbnail_label.grid(row=0, column=3, padx=(15, 5), pady=(25, 0), sticky="nsew")

        self.invert_switch = customtkinter.CTkSwitch(self.edit_image.tab("Filters"), text="invert", 
                                                      font=customtkinter.CTkFont(size=13, weight="bold"), command=self.image_filters_invert, variable=self.invert_switch_var, onvalue="on", offvalue="off")
        self.invert_switch.grid(row=2, column=3, padx=(20, 5), pady=(10, 50), sticky="nsew")

        #detail
        self.detail_switch_var = customtkinter.StringVar(value=self.toggle_switch)

        self.detail_thumbnail = customtkinter.CTkImage(light_image=self.enhanced_image.filter(ImageFilter.DETAIL),
                                  dark_image=self.temp_image.filter(ImageFilter.DETAIL),
                                  size=(100, 100))
        self.detail_thumbnail_label = customtkinter.CTkLabel(self.edit_image.tab("Filters"), image=self.detail_thumbnail, text="")
        self.detail_thumbnail_label.grid(row=3, column=1, padx=(15, 60), pady=(15, 0), sticky="nsew")

        self.detail_switch = customtkinter.CTkSwitch(self.edit_image.tab("Filters"), text="detail", 
                                                      font=customtkinter.CTkFont(size=13, weight="bold"), command=self.image_filters_detail, variable=self.detail_switch_var, onvalue="on", offvalue="off")
        self.detail_switch.grid(row=4, column=1, padx=(20, 5), pady=(10, 10), sticky="nsew")

        #solarize
        self.solarize_switch_var = customtkinter.StringVar(value=self.toggle_switch)

        self.solarize_thumbnail = customtkinter.CTkImage(light_image=ImageOps.solarize(Image.open("boat_small.jpg")),
                                  dark_image=ImageOps.solarize(Image.open("boat_small.jpg")),
                                  size=(100, 100))
        self.solarize_thumbnail_label = customtkinter.CTkLabel(self.edit_image.tab("Filters"), image=self.solarize_thumbnail, text="")
        self.solarize_thumbnail_label.grid(row=3, column=2, padx=(15, 60), pady=(15, 0), sticky="nsew")

        self.solarize_switch = customtkinter.CTkSwitch(self.edit_image.tab("Filters"), text="solarize", 
                                                      font=customtkinter.CTkFont(size=13, weight="bold"), command=self.image_filters_solarize, variable=self.solarize_switch_var, onvalue="on", offvalue="off")
        self.solarize_switch.grid(row=4, column=2, padx=(20, 5), pady=(10, 10), sticky="nsew")


        #emboss
        self.emboss_switch_var = customtkinter.StringVar(value=self.toggle_switch)

        self.emboss_thumbnail = customtkinter.CTkImage(light_image=Image.open("boat_small.jpg").filter(ImageFilter.EMBOSS),
                                  dark_image=Image.open("boat_small.jpg").filter(ImageFilter.EMBOSS),
                                  size=(100, 100))
        self.emboss_thumbnail_label = customtkinter.CTkLabel(self.edit_image.tab("Filters"), image=self.emboss_thumbnail, text="")
        self.emboss_thumbnail_label.grid(row=3, column=3, padx=(15, 5), pady=(15, 0), sticky="nsew")

        self.emboss_switch = customtkinter.CTkSwitch(self.edit_image.tab("Filters"), text="emboss", 
                                                      font=customtkinter.CTkFont(size=13, weight="bold"), command=self.image_filters_emboss, variable=self.emboss_switch_var, onvalue="on", offvalue="off")
        self.emboss_switch.grid(row=4, column=3, padx=(20, 5), pady=(10, 10), sticky="nsew")


        # create checkbox and switch frame
        self.config_image_frame = customtkinter.CTkFrame(self)
        self.config_image_frame.grid(row=1, column=3, padx=(20, 20), pady=(0, 20), sticky="nsew")

        #rotate
        self.image_rotate_label = customtkinter.CTkLabel(master=self.config_image_frame, text="Rotate Image:")
        self.image_rotate_label.grid(row=0, column=0, padx=(20, 10), pady=(30, 10))

        self.image_rotate_option = customtkinter.CTkOptionMenu(master=self.config_image_frame, values=["0°", "45°", "90°", "180°"],
                                                               command=self.rotate_image)
        self.image_rotate_option.grid(row=1, column=0, pady=(0, 10), padx=(20, 10), sticky="n")

        #Mirror Image
        self.image_mirror_label = customtkinter.CTkLabel(master=self.config_image_frame, text="Flips & Mirror:")
        self.image_mirror_label.grid(row=0, column=1, padx=(10, 10), pady=(30, 10))

        self.image_mirrorNflips_option = customtkinter.CTkOptionMenu(master=self.config_image_frame, values=["None", "Flips", "Mirror"],
                                                               command=self.mirrorNflips)
        self.image_mirrorNflips_option.grid(row=1, column=1, pady=(0, 10), padx=(10, 10), sticky="n")

        
        #SCALE
        self.image_scale_label = customtkinter.CTkLabel(master=self.config_image_frame, text="Image Scale:")
        self.image_scale_label.grid(row=0, column=2, padx=(10, 10), pady=(30, 10))

        self.image_scale_option = customtkinter.CTkOptionMenu(master=self.config_image_frame, values=["100%", "80%", "60%", "40%"],
                                                              command=self.image_scale)
        self.image_scale_option.grid(row=1, column=2, pady=(0, 10), padx=(10, 20), sticky="n")
        
        self.appearance_mode_optionemenu.set("Dark")
  
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def image_manipulation(self, value):

        #Sharpness
        sharpness = float(self.sharpness_slider.get())
        sharpness_enhancer = ImageEnhance.Sharpness(self.enhanced_image)
        self.enhanced_image = sharpness_enhancer.enhance(sharpness)

        #Brightness
        brightness = float(self.brightness_slider.get())
        brightness_enhancer = ImageEnhance.Brightness(self.enhanced_image)
        self.enhanced_image = brightness_enhancer.enhance(brightness)

        #COLOR
        color = float(self.color_slider.get())
        color_enhancer = ImageEnhance.Color(self.enhanced_image)
        self.enhanced_image = color_enhancer.enhance(color)

        #CONTRAST
        contrast = float(self.contrast_slider.get())
        contrast_enhancer = ImageEnhance.Contrast(self.enhanced_image)
        self.enhanced_image= contrast_enhancer.enhance(contrast)

        #BLUR
        blur = float(self.blur_slider.get())
        blurred_image = self.enhanced_image.filter(ImageFilter.GaussianBlur(blur))
        self.enhanced_image = blurred_image

        self.my_image = customtkinter.CTkImage(light_image=self.enhanced_image,
                            dark_image=self.enhanced_image,
                            size=(600, 600))
        self.image_label.configure(image=self.my_image)
        self.image_label.image = self.my_image

        
    def image_filters_grayscale(self):

        #GRAYSCALE
        if self.grayscale_switch_var.get() == "on":
            grayscale_image = ImageOps.grayscale(self.enhanced_image)
            self.enhanced_image = grayscale_image
        else:
            self.enhanced_image = self.temp_image
            self.toggle_switch = "off"

        self.my_image = customtkinter.CTkImage(light_image=self.enhanced_image,
                            dark_image=self.enhanced_image,
                            size=(600, 600))
        self.image_label.configure(image=self.my_image)
        self.image_label.image = self.my_image


    def image_filters_invert(self):

        if self.invert_switch_var.get() == "on":
            invert_image = ImageOps.invert(self.enhanced_image)
            self.enhanced_image = invert_image
        else:
            self.enhanced_image = self.temp_image
            self.toggle_switch = "off"
            
        self.my_image = customtkinter.CTkImage(light_image=self.enhanced_image,
                            dark_image=self.enhanced_image,
                            size=(600, 600))
        self.image_label.configure(image=self.my_image)
        self.image_label.image = self.my_image


    def image_filters_posterize(self):

        if self.posterize_switch_var.get() == "on":
            posterize_image = ImageOps.posterize(self.enhanced_image, 2)
            self.enhanced_image = posterize_image
        else:
            self.enhanced_image = self.temp_image
            self.toggle_switch = "off"

        self.my_image = customtkinter.CTkImage(light_image=self.enhanced_image,
                            dark_image=self.enhanced_image,
                            size=(600, 600))
        self.image_label.configure(image=self.my_image)
        self.image_label.image = self.my_image


    def image_filters_detail(self):

        if self.detail_switch_var.get() == "on":
            detail_image = self.enhanced_image.filter(ImageFilter.DETAIL)
            self.enhanced_image = detail_image
        else:
            self.enhanced_image = self.temp_image
            self.toggle_switch = "off"

        self.my_image = customtkinter.CTkImage(light_image=self.enhanced_image,
                            dark_image=self.enhanced_image,
                            size=(600, 600))
        self.image_label.configure(image=self.my_image)
        self.image_label.image = self.my_image
        

    def image_filters_solarize(self):

        if self.solarize_switch_var.get() == "on":
            solarize_image = ImageOps.solarize(self.enhanced_image)
            self.enhanced_image = solarize_image
        else:
            self.enhanced_image = self.temp_image
            self.toggle_switch = "off"
            
        self.my_image = customtkinter.CTkImage(light_image=self.enhanced_image,
                            dark_image=self.enhanced_image,
                            size=(600, 600))
        self.image_label.configure(image=self.my_image)
        self.image_label.image = self.my_image

        
    def image_filters_emboss(self):

        if self.emboss_switch_var.get() == "on":
            emboss_image = self.enhanced_image.filter(ImageFilter.EMBOSS)
            self.enhanced_image = emboss_image
        else:
            self.enhanced_image = self.temp_image
            self.toggle_switch = "off"

        self.my_image = customtkinter.CTkImage(light_image=self.enhanced_image,
                            dark_image=self.enhanced_image,
                            size=(600, 600))
        self.image_label.configure(image=self.my_image)
        self.image_label.image = self.my_image

    
    def open_image(self):
            self.file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg")])
            if self.file_path:
                self.enhanced_image = Image.open(self.file_path)
                self.temp_image = self.enhanced_image

            self.brightness_slider.set(1)
            self.sharpness_slider.set(1)
            self.color_slider.set(1)
            self.contrast_slider.set(1)
            self.blur_slider.set(0.0)

            self.posterize_switch.deselect()
            self.grayscale_switch.deselect()
            self.invert_switch.deselect()
            self.detail_switch.deselect()
            self.solarize_switch.deselect()
            self.emboss_switch.deselect()

            self.image_rotate_option.set("0°")

            self.my_image = customtkinter.CTkImage(light_image=self.enhanced_image,
                    dark_image=self.enhanced_image,
                    size=(600, 600))
            self.image_label.configure(image=self.my_image)
            self.image_label.image = self.my_image


    def reset_image(self):
            self.enhanced_image = Image.open("boat.jpg")
            self.temp_image = self.enhanced_image

            self.brightness_slider.set(1)
            self.sharpness_slider.set(1)
            self.color_slider.set(1)
            self.contrast_slider.set(1)
            self.blur_slider.set(0.0)

            self.posterize_switch.deselect()
            self.grayscale_switch.deselect()
            self.invert_switch.deselect()
            self.detail_switch.deselect()
            self.solarize_switch.deselect()
            self.emboss_switch.deselect()

            self.image_rotate_option.set("0°")

            self.my_image = customtkinter.CTkImage(light_image=self.enhanced_image,
                    dark_image=self.enhanced_image,
                    size=(600, 600))
            self.image_label.configure(image=self.my_image)
            self.image_label.image = self.my_image
        

    def save_image(self):
        save_image_name = customtkinter.CTkInputDialog(text="Masukan nama file (tanpa ekstensi file)", title="Save Image Name")
        self.enhanced_image.save(save_image_name.get_input() + ".jpg")
    

    def rotate_image(self, choice: str):
        
        if choice == "45°":
  
            rotate_image_result = self.enhanced_image.rotate(45)
            self.enhanced_image = rotate_image_result
            
        elif choice == "90°":

            rotate_image_result = self.enhanced_image.rotate(90)
            self.enhanced_image = rotate_image_result
 
        elif choice == "180°":
      
            rotate_image_result = self.enhanced_image.rotate(180)
            self.enhanced_image = rotate_image_result

        else:
            self.enhanced_image = self.temp_image
        
        self.my_image = customtkinter.CTkImage(light_image=self.enhanced_image,
                dark_image=self.enhanced_image, size=(600, 600))
        self.image_label.configure(image=self.my_image)
        self.image_label.image = self.my_image

    def mirrorNflips(self, choice: str):

        if choice == "Flips":
            flips_image_result = ImageOps.flip(self.enhanced_image)
            self.enhanced_image = flips_image_result
        
        elif choice == "Mirror":
            mirror_image_result = ImageOps.mirror(self.enhanced_image)
            self.enhanced_image = mirror_image_result
        
        else:
            self.enhanced_image = self.temp_image

        self.my_image = customtkinter.CTkImage(light_image=self.enhanced_image,
                dark_image=self.enhanced_image, size=(600, 600))
        self.image_label.configure(image=self.my_image)
        self.image_label.image = self.my_image

    def image_scale(self, choice: str):

        if choice == "80%":
            image_scale_result = ImageOps.scale(self.enhanced_image, 0.8, resample=Image.LANCZOS)
            self.enhanced_image = image_scale_result
            image_size = 480
            

        elif choice == "60%":
            image_scale_result = ImageOps.scale(self.enhanced_image, 0.6, resample=Image.LANCZOS)
            self.enhanced_image = image_scale_result
            image_size = 360

        elif choice == "40%":
            image_scale_result = ImageOps.scale(self.enhanced_image, 0.4, resample=Image.LANCZOS)
            self.enhanced_image = image_scale_result
            image_size = 240

        else:
            self.enhanced_image = self.temp_image
            image_size = 600

        self.my_image = customtkinter.CTkImage(light_image=self.enhanced_image,
                dark_image=self.enhanced_image, size=(image_size, image_size))
        self.image_label.configure(image=self.my_image)
        self.image_label.image = self.my_image
        

        
if __name__ == "__main__":
    app = App()
    app.mainloop()