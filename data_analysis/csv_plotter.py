import pandas as pd
import matplotlib.pyplot as plt
import sys

def plot_csv_data(filename):
    try:
        # Read CSV file without headers
        df = pd.read_csv(filename, header=None)
        print(f"Loaded data with {len(df)} samples and {len(df.columns)} columns")
        
        # Create the plot
        plt.figure(figsize=(12, 8))
        
        # Default series names (can be customized here)
        series_names = ['s1', 's2', 's3']
        
        # Plot each column and calculate standard deviation
        print("\nStandard Deviations:")
        print("-" * 30)
        
        for i, col in enumerate(df.columns):
            # Use default name if we have enough, otherwise use column index
            name = series_names[i] if i < len(series_names) else f'col{i}'
            
            # Plot the data
            plt.plot(df.index, df[col], label=name, linewidth=1.5)
            
            # Calculate and print standard deviation
            std_dev = df[col].std()
            mean_val = df[col].mean()
            print(f"{name}: σ = {std_dev:.2f}, μ = {mean_val:.2f}")
        
        # Customize the plot
        plt.xlabel('Sample Number')
        plt.ylabel('ADC Value (12-bit)')
        plt.title('ADC Data Collection')
        plt.ylim(0, 4100)
        plt.xlim(0,len(df))
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        # Show the plot
        plt.tight_layout()
        plt.show()
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except pd.errors.EmptyDataError:
        print(f"Error: File '{filename}' is empty!")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    # Get filename from command line argument or prompt user
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter CSV filename: ")
    
    plot_csv_data(filename)