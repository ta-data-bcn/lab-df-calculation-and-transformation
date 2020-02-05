import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#HACK
#year = 2002

def acquire():
	data_csv = pd.read_csv('vehicles.csv')
	hello_world()
	return data_csv 

def wrangle(data, year):
	#filtered = data[ data.Year == 2001 ]
	filtered = data[ data.Year == year ]
	return filtered
	
def analyze(data_yazan):
	grouped = data_yazan.groupby('Make').agg({'City MPG':'mean'}).reset_index()
	result = grouped.sort_values('City MPG', ascending=False).head(10)
	return result

def report(result, year):
	fig, ax = plt.subplots(figsize=(15,8))
	barchart = sns.barplot(data=result, x='Make', y='City MPG')
	plt.title(f'Top 10 fuel efficient Makes in {year}', fontsize=16)
	return barchart

def save_report(barchart, year):
	fig = barchart.get_figure()
	fig.savefig(f'Top10_{year}.png')

def hello_world():
	print('hello world')

if __name__ == '__main__':
	print('Today we going to extract a top 10 make list')
	print('hello class')

	year_start = int(input('Enter the from year: '))
	year_end = int(input('Enter the to year: '))

	#DATA PIPELINE	
	# Acquisition
	data_anna = acquire()

	for current_year in range(year_start, year_end+1):
		print(current_year)

		# Wrangling
		filtered_rebecca = wrangle(data_anna, current_year)
		# Analysis
		analysed_zak = analyze(filtered_rebecca)
		# Reporting
		report_miguel = report(analysed_zak, current_year)
		save_report(report_miguel, current_year)
	
	print('Data pipeline completed, have a nice day.')
