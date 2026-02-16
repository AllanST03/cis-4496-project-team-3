from tkinter import *
from tkinter import ttk


# Window setup
window = Tk()
window.geometry("1024x768")
window.title("Cancer Pharmacogenomics Dashboard")
window.config(background="#4b40b6")
# Icon + title image
ICON_PATH = r"C:\Users\shibu\OneDrive\Desktop\ALLAN\cis-4496-project-team-3\Code\GUI\Helix.png"   # This shoul changed based on the system, this is only for me

icon = PhotoImage(file=ICON_PATH)
window.iconphoto(True, icon)

# Title Label with image
photo_Label = PhotoImage(file=ICON_PATH)
photo_Label = photo_Label.subsample(20, 20)  # resize image
Titlelabel = Label(
    window,
    text="Welcome to the Cancer Pharmacogenomics Dashboard!",
    font=("Arial", 16),
    bg="#4b40b6",
    fg="white",
    image=photo_Label,
    compound="left" )
Titlelabel.pack(pady=20)

# Ui design
style = ttk.Style()
style.theme_use("default")
style.configure("TFrame", background="#4b40b6")

style.configure("TLabel", background="#4b40b6", foreground="white", font=("Arial", 12)) # input labels
style.configure("Header.TLabel", background="#4b40b6", foreground="white", font=("Impact", 13, "bold")) #???
style.configure("TEntry", fieldbackground="#978EC1", foreground="black") # for the entry input
style.configure("TCombobox", fieldbackground="#978EC1", foreground="black") # for the dropdowns
style.configure("TRadiobutton", background="#4b40b6", foreground="white") # for the this or that options
style.configure("TButton", font=("Arial", 11, "bold")) # for the buttons (run/clear)


# Main form frame (grid layout)
form = ttk.Frame(window, padding=20)
form.pack(fill="x", padx=60)

# section header label
def section_title(row, text):
    lbl = ttk.Label(form, text=text, style="Header.TLabel")
    lbl.grid(row=row, column=0, columnspan=3, sticky="w", pady=(16, 6))
    lbl.configure(font=("Ink Free", 14, "bold"))
    return row + 1

# Assigning variables to each input field
age_var = IntVar(value=30)
sex_var = StringVar(value="Male")  # "Male" or "Female"
tumor_size_var = StringVar(value="")   # numeric text
tumor_stage_var = StringVar(value="")  # numeric text
metastasis_var = StringVar(value="No")     # "Yes" or "No"
neutropenia_var = StringVar(value="No")    # "Yes" or "No"
dosage_var = StringVar(value="")  # numeric text
nausea_var = IntVar(value=1)  # 1 to 4
mutation_var = StringVar(value="EGFR")

# Cancer Type
C_Type = [ "Colon",
        "Leukemia",
        "Lymphoma",
        "Breast",
        "Lung"]
Cancer_Type_var = StringVar(value=C_Type[0])  # default = first item

# Cancer Regimen Options (PLACEHOLDERS) I didn't know what to put here
REGIMEN_OPTIONS = [
    "AC (Doxorubicin + Cyclophosphamide)",
    "TC (Docetaxel + Cyclophosphamide)",
    "FOLFOX",
    "FOLFIRI",
    "FOLFIRINOX",
    "CHOP",
    "R-CHOP",
    "GemCarbo (Gemcitabine + Carboplatin)",
    "GC (Gemcitabine + Cisplatin)"
]
regimen_var = StringVar(value=REGIMEN_OPTIONS[0])  # default = first item

# Mutation Options (FIXED as you requested)
MUTATION_OPTIONS = ["EGFR", "TP53", "KRAS", "DPYD", "BRCA1"] # Default mutations for now


# Row builder helpers
current_row = 0


# Age: Scale + Spinbox (drag OR select)
current_row = section_title(current_row, "Patient Information")
ttk.Label(form, text="Age (drag or select):").grid(row=current_row, column=0, sticky="w", pady=6)

age_scale = ttk.Scale(
    form,
    from_=0, to=100,  # EDIT RANGE HERE if you want (e.g., 0..120)
    orient="horizontal",
    command=lambda v: age_var.set(int(float(v)))
)
age_scale.grid(row=current_row, column=1, sticky="ew", padx=10)

age_spin = Spinbox(
    form,
    from_=0, to=100,  
    textvariable=age_var,
    width=6,
    font=("Arial", 11) )


age_spin.grid(row=current_row, column=2, sticky="w")
current_row += 1

# Keep scale synced with spinbox changes
def sync_age(*args):
    age_scale.set(age_var.get())
age_var.trace_add("write", sync_age)
age_scale.set(age_var.get())
form.columnconfigure(1, weight=1)

# Sex: Male/Female
ttk.Label(form, text="Sex:").grid(row=current_row, column=0, sticky="w", pady=6)
sex_frame = ttk.Frame(form)
sex_frame.grid(row=current_row, column=1, columnspan=2, sticky="w")
ttk.Radiobutton(sex_frame, text="Male", variable=sex_var, value="Male").grid(row=0, column=0, padx=(0, 18))
ttk.Radiobutton(sex_frame, text="Female", variable=sex_var, value="Female").grid(row=0, column=1)
current_row += 1

# Cancer type (single select dropdown) --- Just a place holder information
ttk.Label(form, text="Cancer Type (choose one):").grid(row=current_row, column=0, sticky="w", pady=6)
Cancer_Type_box = ttk.Combobox(
    form,
    textvariable=Cancer_Type_var,
    values=C_Type,   # EDIT PLACEHOLDERS HERE
    state="readonly",
    width=45 )
Cancer_Type_box.grid(row=current_row, column=1, columnspan=2, sticky="w")
current_row += 1

# Tumor Size (Entry)
ttk.Label(form, text="Tumor size (cm):").grid(row=current_row, column=0, sticky="w", pady=6)
tumor_size_entry = ttk.Entry(form, textvariable=tumor_size_var, width=20)
tumor_size_entry.grid(row=current_row, column=1, columnspan=2, sticky="w")
current_row += 1

# Tumor Stage (1 to 4)
ttk.Label(form, text="Tumor stage (number):").grid(row=current_row, column=0, sticky="w", pady=6)
tumor_stage_entry = ttk.Entry(form, textvariable=tumor_stage_var, width=20)
tumor_stage_entry.grid(row=current_row, column=1, columnspan=2, sticky="w")
current_row += 1


# Metastasis: Yes/No
ttk.Label(form, text="Metastasis:").grid(row=current_row, column=0, sticky="w", pady=6)
meta_frame = ttk.Frame(form)
meta_frame.grid(row=current_row, column=1, columnspan=2, sticky="w")
ttk.Radiobutton(meta_frame, text="Yes", variable=metastasis_var, value="Yes").grid(row=0, column=0, padx=(0, 18))
ttk.Radiobutton(meta_frame, text="No", variable=metastasis_var, value="No").grid(row=0, column=1)
current_row += 1


# Treatment / Regimen Section
current_row = section_title(current_row, "Treatment of the Cancer")


# Cancer regimen (single select dropdown) --- Just a place holder information
ttk.Label(form, text="Cancer regimen (choose one):").grid(row=current_row, column=0, sticky="w", pady=6)
regimen_box = ttk.Combobox(
    form,
    textvariable=regimen_var,
    values=REGIMEN_OPTIONS,   # EDIT PLACEHOLDERS HERE
    state="readonly",
    width=45 )
regimen_box.grid(row=current_row, column=1, columnspan=2, sticky="w")
current_row += 1

# Dosage (Entry)
ttk.Label(form, text="Dosage (centigray 'cGy'):").grid(row=current_row, column=0, sticky="w", pady=6)
dosage_entry = ttk.Entry(form, textvariable=dosage_var, width=20)
dosage_entry.grid(row=current_row, column=1, columnspan=2, sticky="w")
current_row += 1


# Side Effects Section
current_row = section_title(current_row, "Side Effects / Outcomes")


# Nausea 1–4 (single select)
ttk.Label(form, text="Nausea (1 to 4):").grid(row=current_row, column=0, sticky="w", pady=6)
nausea_box = ttk.Combobox(
    form,
    textvariable=nausea_var,
    values=[1, 2, 3, 4],    # Range here
    state="readonly",
    width=10 )
nausea_box.grid(row=current_row, column=1, columnspan=2, sticky="w")
current_row += 1

# Neutropenia Yes/No
ttk.Label(form, text="Neutropenia:").grid(row=current_row, column=0, sticky="w", pady=6)
neutro_frame = ttk.Frame(form)
neutro_frame.grid(row=current_row, column=1, columnspan=2, sticky="w")
ttk.Radiobutton(neutro_frame, text="Yes", variable=neutropenia_var, value="Yes").grid(row=0, column=0, padx=(0, 18))
ttk.Radiobutton(neutro_frame, text="No", variable=neutropenia_var, value="No").grid(row=0, column=1)
current_row += 1


# Pharmacogenomics Section -- jUST A HEADER
current_row = section_title(current_row, "Pharmacogenomics")


# Mutation type (single select)
ttk.Label(form, text="Mutation type:").grid(row=current_row, column=0, sticky="w", pady=6)
mutation_box = ttk.Combobox(
    form,
    textvariable=mutation_var,
    values=MUTATION_OPTIONS,  # DO NOT CHANGE unless you want different genes
    state="readonly",
    width=12 )
mutation_box.grid(row=current_row, column=1, columnspan=2, sticky="w")
current_row += 1


# Buttons
btn_frame = ttk.Frame(window, padding=20)
btn_frame.pack(fill="x", padx=60)

def submit_form():
    """
    Collect all inputs and print them.
    """
    data = {
        "Age": age_var.get(),
        "Sex": sex_var.get(),
        "TumorSize": tumor_size_var.get(),
        "TumorStage": tumor_stage_var.get(),
        "Metastasis": metastasis_var.get(),
        "CancerRegimen": regimen_var.get(),
        "Dosage": dosage_var.get(),
        "Nausea": nausea_var.get(),
        "Neutropenia": neutropenia_var.get(),
        "MutationType": mutation_var.get(),
    }
    print("\n--- Form Submission ---")
    for k, v in data.items():
        print(f"{k}: {v}")

def clear_form():
    """Reset everything back to defaults."""
    age_var.set(30)
    sex_var.set("Male")
    tumor_size_var.set("")
    tumor_stage_var.set("")
    metastasis_var.set("No")
    regimen_var.set(REGIMEN_OPTIONS[0])
    dosage_var.set("")
    nausea_var.set(1)
    neutropenia_var.set("No")
    mutation_var.set("EGFR")

ttk.Button(btn_frame, text="Run Prediction", command=submit_form).pack(side=RIGHT, padx=(10, 0))
ttk.Button(btn_frame, text="Clear", command=clear_form).pack(side=RIGHT)

# Dont change anything belowe, this is just for running the window
# Run the window

window.mainloop()
