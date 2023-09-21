import tkinter as tk
from tkinter import ttk
import math


class LoanCalculatorApp:

  def __init__(self, root):
    self.root = root
    root.title("Loan Calculator")
    self.setup_ui()
    self.default_values()

  def setup_ui(self):
    # Create a custom style with your preferred colors
    custom_style = ttk.Style()
    custom_style.configure('Custom.TLabel', foreground='blue')
    custom_style.configure('Custom.TEntry', foreground='green')
    custom_style.configure('Custom.TButton',
                           foreground='white',
                           background='blue')

    # Create labels and entry fields for user inputs
    self.label_principal = ttk.Label(self.root,
                                     text="Principal:",
                                     style='Custom.TLabel')
    self.label_principal.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    self.entry_principal = ttk.Entry(self.root,
                                     justify="center",
                                     style='Custom.TEntry')
    self.entry_principal.grid(row=0, column=1, padx=10, pady=5)

    self.label_monthly_payment = ttk.Label(self.root,
                                           text="Monthly Payment:",
                                           style='Custom.TLabel')
    self.label_monthly_payment.grid(row=1,
                                    column=0,
                                    padx=10,
                                    pady=5,
                                    sticky="w")
    self.entry_monthly_payment = ttk.Entry(self.root,
                                           justify="center",
                                           style='Custom.TEntry')
    self.entry_monthly_payment.grid(row=1, column=1, padx=10, pady=5)

    self.label_interest_rate = ttk.Label(self.root,
                                         text="Annual Interest Rate (%):",
                                         style='Custom.TLabel')
    self.label_interest_rate.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    self.entry_interest_rate = ttk.Entry(self.root,
                                         justify="center",
                                         style='Custom.TEntry')
    self.entry_interest_rate.grid(row=2, column=1, padx=10, pady=5)

    self.label_loan_term_months = ttk.Label(self.root,
                                            text="Loan Term (months):",
                                            style='Custom.TLabel')
    self.label_loan_term_months.grid(row=3,
                                     column=0,
                                     padx=10,
                                     pady=5,
                                     sticky="w")
    self.entry_loan_term_months = ttk.Entry(self.root,
                                            justify="center",
                                            style='Custom.TEntry')
    self.entry_loan_term_months.grid(row=3, column=1, padx=10, pady=5)

    self.label_down_payment = ttk.Label(self.root,
                                        text="Down Payment:",
                                        style='Custom.TLabel')
    self.label_down_payment.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    self.entry_down_payment = ttk.Entry(self.root,
                                        justify="center",
                                        style='Custom.TEntry')
    self.entry_down_payment.grid(row=4, column=1, padx=10, pady=5)

    self.button_calculate = ttk.Button(self.root,
                                       text="Calculate",
                                       command=self.calculate_loan,
                                       style='Custom.TButton')
    self.button_calculate.grid(row=5, columnspan=2, pady=10)

    self.result_frame = ttk.LabelFrame(self.root,
                                       text="Results",
                                       style='Custom.TLabel')
    self.result_frame.grid(row=6, columnspan=2, padx=10, pady=5, sticky="ew")

    self.label_principal_result = ttk.Label(self.result_frame,
                                            text="",
                                            style='Custom.TLabel')
    self.label_principal_result.grid(row=0,
                                     column=0,
                                     padx=10,
                                     pady=5,
                                     sticky="w")

    self.label_monthly_payment_result = ttk.Label(self.result_frame,
                                                  text="",
                                                  style='Custom.TLabel')
    self.label_monthly_payment_result.grid(row=1,
                                           column=0,
                                           padx=10,
                                           pady=5,
                                           sticky="w")

    self.label_interest_rate_result = ttk.Label(self.result_frame,
                                                text="",
                                                style='Custom.TLabel')
    self.label_interest_rate_result.grid(row=2,
                                         column=0,
                                         padx=10,
                                         pady=5,
                                         sticky="w")

    self.label_loan_term_months_result = ttk.Label(self.result_frame,
                                                   text="",
                                                   style='Custom.TLabel')
    self.label_loan_term_months_result.grid(row=3,
                                            column=0,
                                            padx=10,
                                            pady=5,
                                            sticky="w")

  def default_values(self):
    # Set default values to 0
    self.entry_principal.insert(0, "0")
    self.entry_monthly_payment.insert(0, "0")
    self.entry_interest_rate.insert(0, "0")
    self.entry_loan_term_months.insert(0, "0")
    self.entry_down_payment.insert(0, "0")

  def calculate_loan(self):
    try:
      # Get input values
      principal = float(self.entry_principal.get())
      monthly_payment = float(self.entry_monthly_payment.get())
      interest_rate = float(self.entry_interest_rate.get()) / 100.0
      loan_term_months = int(self.entry_loan_term_months.get())
      down_payment = float(self.entry_down_payment.get())

      # Calculate the monthly interest rate
      monthly_interest_rate = interest_rate / 12.0

      # Calculate the missing field
      if principal == 0:
        principal = (monthly_payment * ((1 + monthly_interest_rate) ** loan_term_months - 1)) / \
                    (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term_months) + down_payment
      elif monthly_payment == 0:
        monthly_payment = (principal - down_payment) * (monthly_interest_rate) / \
                          (1 - (1 + monthly_interest_rate) ** -loan_term_months)
      elif interest_rate == 0:
        interest_rate = 12 * ((
            (monthly_payment /
             (principal - down_payment))**(1 / loan_term_months)) - 1)
      elif loan_term_months == 0:
        loan_term_months = abs(
            -math.log(1 - ((principal - down_payment) * monthly_interest_rate /
                           monthly_payment)) /
            (math.log(1 + monthly_interest_rate)))

      # Update the result labels
      self.label_principal_result.config(text=f"Principal: ${principal:.2f}")
      self.label_monthly_payment_result.config(
          text=f"Monthly Payment: ${monthly_payment:.2f}")
      self.label_interest_rate_result.config(
          text=f"Annual Interest Rate: {interest_rate * 100:.2f}%")
      self.label_loan_term_months_result.config(
          text=f"Loan Term (months): {loan_term_months:.2f} months")

    except ValueError:
      # Display an error message
      self.label_principal_result.config(text="Please enter valid numbers.")


if __name__ == "__main__":
  root = tk.Tk()
  app = LoanCalculatorApp(root)
  root.mainloop()
