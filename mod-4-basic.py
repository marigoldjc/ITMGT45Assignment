#!/usr/bin/env python
# coding: utf-8

# ### Assignment: Python (Basic)
# #### Useful Business Calculations
# ##### Savings

# In[4]:


def savings(gross_pay, tax_rate, expenses):
    gp_tax = gross_pay - (int(gross_pay * tax_rate)) #after tax
    rsavings = gp_tax - expenses #after tax and expenses
    return rsavings


# In[5]:


gross_pay = float(input("Gross pay per month: "))

tax_rate = float(input("Tax rate per month in decimal: "))
                 
expenses = float(input("Expenses per month: "))

takehome = savings(gross_pay, tax_rate, expenses)

print("Your take-home pay per month is", takehome)


# ##### Material Waste

# In[6]:


def material_waste(total_material, material_units, num_jobs, job_consumption):
    waste_set_jobs = total_material - (job_consumption * num_jobs)
    return waste_set_jobs


# In[8]:


total_material = int(input("Enter the total amount of material available: "))

material_units = str(input("Unit to express the quantity of the material: "))

num_jobs = int(input("Enter the number of jobs to run: "))

job_consumption = int(input("Enter the amount of material consumed per job: "))

waste = material_waste(total_material, material_units, num_jobs, job_consumption)

print(waste, material_units)


# ##### Interest

# In[3]:


def interest(principal, rate, periods):
    final_value = principal + (principal * (rate * periods))
    return int(final_value)


# In[14]:


principal = float(input("Enter amount invested: "))

rate = float(input("Enter interest rate per year: "))

periods = int(input("Enter number of years invested: "))

final = interest(principal, rate, periods)

print("The final value of the investment after", periods, "years is", final, ".")


# ##### Body Mass Index

# In[1]:


def body_mass_index(weight, height):
    kg = weight * 0.453592
    m = (height[0] * 0.3048) + (height[1]*0.0254)
    
    bmi = kg / (m**2)
    
    return bmi


# In[2]:


weight = float(input("Enter your weight in pounds: "))

n = 2
height = list(map(int, input("Enter your height, foot then inches: ").strip().split()))[:n]

bmi = body_mass_index(weight, height)
print("Your BMI:", bmi)

