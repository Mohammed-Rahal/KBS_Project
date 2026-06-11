import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import sys
import os
from src.engine import GiftRecommender

# Handle both script and frozen executable paths
if getattr(sys, "frozen", False):
    # Running as compiled executable
    base_path = sys._MEIPASS  # type: ignore
else:
    # Running as script
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, base_path)


class GiftRecommenderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎁 Gift Recommender System")
        self.root.geometry("1000x700")
        self.root.minsize(900, 650)

        # Initialize engine
        self.engine = GiftRecommender()
        self.available_interests = self.engine.get_available_interests()

        # Configure style
        self.setup_styles()

        # Build UI
        self.create_widgets()

    def setup_styles(self):
        """Configure ttk styles"""
        style = ttk.Style()
        style.theme_use("clam")

        # Configure colors
        self.colors = {
            "bg": "#f0f4f8",
            "primary": "#2c5282",
            "secondary": "#4299e1",
            "accent": "#48bb78",
            "text": "#2d3748",
            "light": "#e2e8f0",
            "white": "#ffffff",
            "danger": "#c53030",
        }

        self.root.configure(bg=self.colors["bg"])

    def create_widgets(self):
        """Create all GUI widgets"""
        # Title Bar
        title_frame = tk.Frame(self.root, bg=self.colors["primary"])
        title_frame.pack(fill=tk.X)

        title_label = tk.Label(
            title_frame,
            text="🎁  Children's Gift Recommendation System",
            font=("Arial", 18, "bold"),
            bg=self.colors["primary"],
            fg="white",
            pady=12,
        )
        title_label.pack()

        # Main content area with two columns
        main_container = tk.Frame(self.root, bg=self.colors["bg"])
        main_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=(15, 0))

        # Left column - Input (make it scrollable)
        left_column = tk.Frame(main_container, bg=self.colors["bg"])
        left_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 8))

        # Right column - Results
        right_column = tk.Frame(main_container, bg=self.colors["bg"])
        right_column.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(8, 0))

        # Create panels
        self.create_input_panel(left_column)
        self.create_results_panel(right_column)

        # Button bar at bottom
        self.create_button_bar()

    def _on_mousewheel(self, event):
        """Mouse wheel scrolling for interests canvas"""
        self.interests_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _bind_mousewheel(self, event):
        """Bind mousewheel to canvas when mouse enters"""
        self.interests_canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mousewheel(self, event):
        """Unbind mousewheel when mouse leaves"""
        self.interests_canvas.unbind_all("<MouseWheel>")

    def create_input_panel(self, parent):
        """Create input panel with scrollbar for entire panel"""
        # Create a frame to hold the panel
        panel_container = tk.Frame(parent, bg=self.colors["bg"])
        panel_container.pack(fill=tk.BOTH, expand=True)

        # Create canvas and scrollbar for the entire input panel
        input_canvas = tk.Canvas(
            panel_container, bg=self.colors["bg"], width=380, highlightthickness=0
        )
        input_scrollbar = ttk.Scrollbar(
            panel_container, orient="vertical", command=input_canvas.yview
        )

        # Frame inside canvas for all input widgets
        input_frame = tk.LabelFrame(
            input_canvas,
            text=" Search Criteria ",
            font=("Arial", 11, "bold"),
            bg=self.colors["white"],
            fg=self.colors["text"],
            padx=12,
            pady=12,
            width=360,
        )

        # Configure canvas
        input_canvas.configure(yscrollcommand=input_scrollbar.set)

        # Pack canvas and scrollbar
        input_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        input_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create window in canvas
        canvas_window = input_canvas.create_window(
            (0, 0), window=input_frame, anchor="nw", width=360
        )

        # Configure canvas to resize with content
        def configure_canvas(event):
            input_canvas.configure(scrollregion=input_canvas.bbox("all"))

        def configure_window(event):
            # Update the width of the window to fit the canvas
            input_canvas.itemconfig(canvas_window, width=event.width)

        input_frame.bind("<Configure>", configure_canvas)
        input_canvas.bind("<Configure>", configure_window)

        # Mousewheel scrolling for the input panel
        def on_enter(event):
            input_canvas.bind_all(
                "<MouseWheel>",
                lambda e: input_canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"),
            )

        def on_leave(event):
            input_canvas.unbind_all("<MouseWheel>")

        input_canvas.bind("<Enter>", on_enter)
        input_canvas.bind("<Leave>", on_leave)
        input_frame.bind("<Enter>", on_enter)
        input_frame.bind("<Leave>", on_leave)

        # ===== WIDGETS INSIDE INPUT FRAME =====

        # Age input
        age_frame = tk.Frame(input_frame, bg=self.colors["white"])
        age_frame.pack(fill=tk.X, pady=(0, 10))

        tk.Label(
            age_frame,
            text="👶 Child's Age:",
            font=("Arial", 10, "bold"),
            bg=self.colors["white"],
        ).pack(anchor=tk.W)

        self.age_var = tk.StringVar(value="8")
        age_spinbox = ttk.Spinbox(
            age_frame,
            from_=0,
            to=18,
            textvariable=self.age_var,
            width=8,
            font=("Arial", 10),
        )
        age_spinbox.pack(anchor=tk.W)

        # Gender selection
        gender_frame = tk.Frame(input_frame, bg=self.colors["white"])
        gender_frame.pack(fill=tk.X, pady=(0, 10))

        tk.Label(
            gender_frame,
            text="👤 Gender:",
            font=("Arial", 10, "bold"),
            bg=self.colors["white"],
        ).pack(anchor=tk.W)

        self.gender_var = tk.StringVar(value="any")
        gender_radio_frame = tk.Frame(gender_frame, bg=self.colors["white"])
        gender_radio_frame.pack(anchor=tk.W)

        genders = [("Boy", "male"), ("Girl", "female"), ("Any", "any")]

        for text, value in genders:
            tk.Radiobutton(
                gender_radio_frame,
                text=text,
                variable=self.gender_var,
                value=value,
                bg=self.colors["white"],
                font=("Arial", 9),
            ).pack(side=tk.LEFT, padx=(0, 12))

        # Interests selection
        interests_label_frame = tk.Frame(input_frame, bg=self.colors["white"])
        interests_label_frame.pack(fill=tk.X, pady=(0, 3))

        tk.Label(
            interests_label_frame,
            text="🎨 Interests:",
            font=("Arial", 10, "bold"),
            bg=self.colors["white"],
        ).pack(anchor=tk.W)

        tk.Label(
            interests_label_frame,
            text="(scroll for more)",
            font=("Arial", 8),
            bg=self.colors["white"],
            fg="gray",
        ).pack(anchor=tk.W)

        # Scrollable interests container
        interests_outer = tk.Frame(
            input_frame, bg=self.colors["white"], bd=1, relief=tk.SOLID, height=180
        )
        interests_outer.pack(fill=tk.X, pady=(0, 10))
        interests_outer.pack_propagate(False)  # Fixed height

        self.interests_canvas = tk.Canvas(
            interests_outer, bg=self.colors["white"], highlightthickness=0
        )
        interests_scrollbar = ttk.Scrollbar(
            interests_outer, orient="vertical", command=self.interests_canvas.yview
        )
        self.interests_inner = tk.Frame(self.interests_canvas, bg=self.colors["white"])

        self.interests_inner.bind(
            "<Configure>",
            lambda e: self.interests_canvas.configure(
                scrollregion=self.interests_canvas.bbox("all")
            ),
        )

        self.interests_canvas.create_window(
            (0, 0), window=self.interests_inner, anchor="nw"
        )
        self.interests_canvas.configure(yscrollcommand=interests_scrollbar.set)

        self.interests_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        interests_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Mousewheel for interests
        def on_interests_enter(event):
            self.interests_canvas.bind_all(
                "<MouseWheel>",
                lambda e: self.interests_canvas.yview_scroll(
                    int(-1 * (e.delta / 120)), "units"
                ),
            )

        def on_interests_leave(event):
            self.interests_canvas.unbind_all("<MouseWheel>")

        self.interests_canvas.bind("<Enter>", on_interests_enter)
        self.interests_canvas.bind("<Leave>", on_interests_leave)
        self.interests_inner.bind("<Enter>", on_interests_enter)
        self.interests_inner.bind("<Leave>", on_interests_leave)

        # Create checkboxes for interests in two columns
        self.interest_vars = {}
        mid = len(self.available_interests) // 2 + 1

        for i, interest in enumerate(self.available_interests):
            var = tk.BooleanVar()
            self.interest_vars[interest] = var

            col = 0 if i < mid else 1
            row = i if i < mid else i - mid

            cb = tk.Checkbutton(
                self.interests_inner,
                text=interest.replace("_", " ").title(),
                variable=var,
                bg=self.colors["white"],
                font=("Arial", 9),
                anchor=tk.W,
                padx=5,
            )
            cb.grid(row=row, column=col, sticky=tk.W, pady=1)
            # Make the label clickable too
            cb.bind("<Enter>", on_interests_enter)
            cb.bind("<Leave>", on_interests_leave)

        # Gift type selection
        type_frame = tk.Frame(input_frame, bg=self.colors["white"])
        type_frame.pack(fill=tk.X, pady=(0, 10))

        tk.Label(
            type_frame,
            text="🎁 Gift Type:",
            font=("Arial", 10, "bold"),
            bg=self.colors["white"],
        ).pack(anchor=tk.W)

        self.gift_type_var = tk.StringVar(value="any")
        gift_types = [
            ("Physical", "physical"),
            ("Experience", "experience"),
            ("Activity", "activity"),
            ("Any", "any"),
        ]

        type_radio_frame = tk.Frame(type_frame, bg=self.colors["white"])
        type_radio_frame.pack(anchor=tk.W)

        for text, value in gift_types:
            tk.Radiobutton(
                type_radio_frame,
                text=text,
                variable=self.gift_type_var,
                value=value,
                bg=self.colors["white"],
                font=("Arial", 9),
            ).pack(side=tk.LEFT, padx=(0, 12))

        # Budget input
        budget_frame = tk.Frame(input_frame, bg=self.colors["white"])
        budget_frame.pack(fill=tk.X, pady=(0, 5))

        tk.Label(
            budget_frame,
            text="💰 Maximum Budget ($):",
            font=("Arial", 10, "bold"),
            bg=self.colors["white"],
        ).pack(anchor=tk.W)

        self.budget_var = tk.StringVar(value="50.00")
        budget_entry = ttk.Entry(
            budget_frame, textvariable=self.budget_var, font=("Arial", 10), width=12
        )
        budget_entry.pack(anchor=tk.W)

    def create_results_panel(self, parent):
        """Create results panel"""
        results_frame = tk.LabelFrame(
            parent,
            text=" Recommendations ",
            font=("Arial", 11, "bold"),
            bg=self.colors["white"],
            fg=self.colors["text"],
            padx=12,
            pady=12,
        )
        results_frame.pack(fill=tk.BOTH, expand=True)

        # Results text area
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            wrap=tk.WORD,
            font=("Consolas", 9),
            bg="#f7fafc",
            fg=self.colors["text"],
        )
        self.results_text.pack(fill=tk.BOTH, expand=True)

        # Configure text tags
        self.results_text.tag_configure(
            "header", font=("Arial", 13, "bold"), foreground=self.colors["primary"]
        )
        self.results_text.tag_configure(
            "subheader", font=("Arial", 10, "bold"), foreground=self.colors["text"]
        )
        self.results_text.tag_configure(
            "top_pick", font=("Arial", 10, "bold"), foreground=self.colors["accent"]
        )
        self.results_text.tag_configure("normal", font=("Consolas", 9))
        self.results_text.tag_configure(
            "score_high", foreground="#22543d", font=("Consolas", 9, "bold")
        )
        self.results_text.tag_configure(
            "score_medium", foreground="#975a16", font=("Consolas", 9, "bold")
        )
        self.results_text.tag_configure(
            "score_low", foreground="#9b2c2c", font=("Consolas", 9, "bold")
        )

        # Initial message
        self.results_text.insert(
            tk.END, "\n\n  👈 Fill in your search criteria\n", "subheader"
        )
        self.results_text.insert(
            tk.END, "  and click 'Find Perfect Gift!'\n\n", "normal"
        )
        self.results_text.insert(
            tk.END, "  Or click 'Quick Test' for a demo!\n", "normal"
        )

    def create_button_bar(self):
        """Create button bar at the bottom"""
        button_frame = tk.Frame(self.root, bg=self.colors["bg"])
        button_frame.pack(fill=tk.X, padx=15, pady=10)

        # Left buttons
        left_buttons = tk.Frame(button_frame, bg=self.colors["bg"])
        left_buttons.pack(side=tk.LEFT)

        # Search button
        search_btn = tk.Button(
            left_buttons,
            text="🔍 Find Perfect Gift!",
            command=self.search_gifts,
            font=("Arial", 11, "bold"),
            bg=self.colors["accent"],
            fg="white",
            padx=20,
            pady=8,
            relief=tk.RAISED,
            cursor="hand2",
            borderwidth=2,
        )
        search_btn.pack(side=tk.LEFT, padx=(0, 8))

        # Clear button
        clear_btn = tk.Button(
            left_buttons,
            text="🗑️ Clear All",
            command=self.clear_all,
            font=("Arial", 10),
            bg=self.colors["light"],
            fg=self.colors["text"],
            padx=15,
            pady=8,
            relief=tk.RAISED,
            cursor="hand2",
            borderwidth=2,
        )
        clear_btn.pack(side=tk.LEFT, padx=(0, 8))

        # Quick test button
        test_btn = tk.Button(
            left_buttons,
            text="🧪 Quick Test",
            command=self.quick_test,
            font=("Arial", 10),
            bg=self.colors["secondary"],
            fg="white",
            padx=15,
            pady=8,
            relief=tk.RAISED,
            cursor="hand2",
            borderwidth=2,
        )
        test_btn.pack(side=tk.LEFT)

        # Right buttons
        right_buttons = tk.Frame(button_frame, bg=self.colors["bg"])
        right_buttons.pack(side=tk.RIGHT)

        # Exit button
        exit_btn = tk.Button(
            right_buttons,
            text="👋 Exit",
            command=self.root.quit,
            font=("Arial", 10, "bold"),
            bg=self.colors["danger"],
            fg="white",
            padx=20,
            pady=8,
            relief=tk.RAISED,
            cursor="hand2",
            borderwidth=2,
        )
        exit_btn.pack(side=tk.RIGHT)

    def get_selected_interests(self):
        """Get list of selected interests"""
        return [interest for interest, var in self.interest_vars.items() if var.get()]

    def search_gifts(self):
        """Execute search and display results"""
        # Get input values
        try:
            age = int(self.age_var.get())
            budget = float(self.budget_var.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid age and budget values.")
            return

        gender = self.gender_var.get()
        gift_type = self.gift_type_var.get()
        interests = self.get_selected_interests()

        # Validate
        if not interests:
            messagebox.showwarning("Warning", "Please select at least one interest.")
            return

        if age < 0 or age > 18:
            messagebox.showerror("Error", "Age must be between 0 and 18.")
            return

        if budget <= 0:
            messagebox.showerror("Error", "Budget must be greater than $0.")
            return

        # Clear previous results
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, "🔍 Searching...\n", "subheader")
        self.root.update()

        # Get recommendations
        recommendations = self.engine.recommend(
            age=age,
            interests=interests,
            budget=budget,
            gender=gender,
            gift_type=gift_type,
        )

        # Display results
        self.display_results(recommendations, age, interests, budget, gender, gift_type)

    def display_results(
        self, recommendations, age, interests, budget, gender, gift_type
    ):
        """Display recommendations in the results panel"""
        self.results_text.delete(1.0, tk.END)

        # Header
        self.results_text.insert(tk.END, "🎁 GIFT RECOMMENDATIONS\n", "header")
        self.results_text.insert(tk.END, "─" * 45 + "\n\n", "normal")

        # Search criteria
        self.results_text.insert(tk.END, "📋 Your Criteria:\n", "subheader")
        self.results_text.insert(tk.END, f"  • Age: {age} years\n", "normal")
        self.results_text.insert(
            tk.END, f"  • Gender: {gender.capitalize()}\n", "normal"
        )
        self.results_text.insert(
            tk.END, f"  • Interests: {', '.join(interests)}\n", "normal"
        )
        self.results_text.insert(
            tk.END, f"  • Type: {gift_type.replace('_', ' ').title()}\n", "normal"
        )
        self.results_text.insert(tk.END, f"  • Budget: ${budget:.2f}\n\n", "normal")

        # Results
        if not recommendations:
            self.results_text.insert(
                tk.END, "😕 No matching gifts found.\n\n", "normal"
            )
            self.results_text.insert(tk.END, "💡 Suggestions:\n", "subheader")
            self.results_text.insert(
                tk.END, "  • Try increasing your budget\n", "normal"
            )
            self.results_text.insert(
                tk.END, "  • Try selecting 'Any' gift type\n", "normal"
            )
            self.results_text.insert(
                tk.END, "  • Try selecting more interests\n", "normal"
            )
            return

        self.results_text.insert(
            tk.END, f"📦 Found {len(recommendations)} matching gifts\n\n", "subheader"
        )

        # Show recommendations
        for i, gift in enumerate(recommendations[:8], 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "  "

            score = gift["score"]
            if score >= 70:
                score_tag = "score_high"
            elif score >= 50:
                score_tag = "score_medium"
            else:
                score_tag = "score_low"

            self.results_text.insert(tk.END, f"{medal} ", "normal")
            self.results_text.insert(tk.END, f"{gift['name']}\n", "subheader")
            self.results_text.insert(
                tk.END, f"    {gift['type'].capitalize()} | ", "normal"
            )
            self.results_text.insert(
                tk.END, f"{gift['category'].replace('_', ' ').title()} | ", "normal"
            )
            self.results_text.insert(tk.END, f"${gift['price']:.2f}\n", "normal")

            bar_length = score // 2
            bar = "█" * bar_length + "░" * (50 - bar_length)
            self.results_text.insert(tk.END, f"    Score: ", "normal")
            self.results_text.insert(tk.END, f"{score}/100 ", score_tag)
            self.results_text.insert(tk.END, f"[{bar}]\n\n", score_tag)

        if len(recommendations) > 8:
            self.results_text.insert(
                tk.END, f"  ... and {len(recommendations) - 8} more matches\n", "normal"
            )

        if len(recommendations) > 1:
            prices = [g["price"] for g in recommendations]
            scores = [g["score"] for g in recommendations]

            self.results_text.insert(tk.END, "─" * 45 + "\n", "normal")
            self.results_text.insert(tk.END, "📊 Summary:\n", "subheader")
            self.results_text.insert(
                tk.END,
                f"  • Price Range: ${min(prices):.2f} - ${max(prices):.2f}\n",
                "normal",
            )
            self.results_text.insert(
                tk.END, f"  • Average Price: ${sum(prices)/len(prices):.2f}\n", "normal"
            )
            self.results_text.insert(
                tk.END, f"  • Best Score: {max(scores)}/100\n", "normal"
            )

    def clear_all(self):
        """Clear all inputs and results"""
        self.age_var.set("8")
        self.gender_var.set("any")
        self.gift_type_var.set("any")
        self.budget_var.set("50.00")

        for var in self.interest_vars.values():
            var.set(False)

        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(
            tk.END, "\n\n  👈 Fill in your search criteria\n", "subheader"
        )
        self.results_text.insert(
            tk.END, "  and click 'Find Perfect Gift!'\n\n", "normal"
        )
        self.results_text.insert(
            tk.END, "  Or click 'Quick Test' for a demo!\n", "normal"
        )

    def quick_test(self):
        """Run a quick test search"""
        self.age_var.set("7")
        self.gender_var.set("any")
        self.gift_type_var.set("any")
        self.budget_var.set("40.00")

        for var in self.interest_vars.values():
            var.set(False)

        test_interests = ["science", "experiments", "dinosaurs"]
        for interest in test_interests:
            if interest in self.interest_vars:
                self.interest_vars[interest].set(True)

        self.search_gifts()


def main():
    root = tk.Tk()
    app = GiftRecommenderGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
