def lists():
	global states
	states = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY"]
#########################################################################################
center_string = ""
count = 0
#########################################################################################
from time import clock
#########################################################################################
from os import system, path, get_terminal_size
window_width = get_terminal_size().columns
#########################################################################################
from datetime import date
today = date.today().strftime("%B %d, %Y")
#########################################################################################
from urllib.request import urlopen
link="https://www.census.gov/quickfacts/"
search_phrase="Population, Census, April 1, 2020"
#########################################################################################
def header():
	system("cls||clear")
	print("\n\n"+"{0} {1}".format("Edin Mehanovic CIS125 Structure and Logic", today).center(window_width)+"\n\n")
#########################################################################################
def center(phrase):
	phrase = str(phrase)
	return ('%s'.center(get_terminal_size().columns-len(phrase))%phrase)
#########################################################################################
def input_center (phrase):
	return input("".ljust((window_width - len(phrase))//2)+ phrase)	
#########################################################################################
def formating_process(phrase1,phrase2,phrase3):
	return (center("{0:5} {1:10} {2:10}".format(phrase1,phrase2,phrase3)))
#########################################################################################
def clock_timer():
	global start_time
	start_time = clock()
#########################################################################################
def columns (phrase,col,remaining=False):
	global center_string,count
	if remaining:
		while count %col !=0:
			center_string+=" {0:>29} ".format("")
			count += 1
		print(center(center_string))
		center_string = ""
	else:
		center_string += " {0:>29} ".format(phrase)
		count+=1
		if count %col ==0:
			print(center(center_string))
			center_string = ""
#########################################################################################
def read_url(link, search_phrase):
	f=urlopen(link)
	sp=False
	for line in f:
		line = str(line.strip())
		line = str(line.strip('b'))
		line = str(line.strip("'"))
		result=""
		found = False
		for c in line:
			if c =="<":
				found = True
			if not found:
				result += c
			if c == ">":
				found = False
		if result !="":
			if sp:
				sp = False
				if result[0].isdigit():
					break
			if result == search_phrase:
				sp=True
	f.close()
	return result
#########################################################################################
def process():
	global final_pop, mean_pop,sum, elapsed_sec,elapsed_min
	# Population Portion
	pop = []
	percent_pop = []
	pop_int=[]
	final_pop = []
	sum =0
	print(len(states))
	for i in range(len(states)):
		header()
		print(center("Loading {0} of {1} in progress... ".format(i+1,len(states))))
		link1 = link+states[i]
		pop=read_url(link1,search_phrase)
		pop_int = int(pop.replace(",",""))
		link1 = ""
		sum+= pop_int
		final_pop += [[states[i],pop_int,0]]
	for i in range(len(final_pop)):
		final_state = final_pop[i]
		final_state[2] = final_state[1]/sum
	for j in range(len(final_pop)):
		for i in range(len(final_pop)):
			if final_pop[j][1] > final_pop[i][1]:
				final_pop[j],final_pop[i]=final_pop[i],final_pop[j]
	elapsed = clock() - start_time
	mean_pop = sum/len(states)
	# Clock Portion5
	elapsed_sec = elapsed%60
	elapsed_min = elapsed //60
#########################################################################################
def output():
	header()
	print(center("Population, Census, April, 1 2020"+"\n\n"))
	for i in range(3):
		columns(" {0:<5} {1:>10} {2:>10} ".format('State', 'Population', 'Percentage'), 3 )
	for i in range(3):
		columns(" {0:<5} {1:>10} {2:>10} ".format("="*5,"="*10,"="*10),3)
	for a in range(len(final_pop)):
		final_state = final_pop[a]
		columns(" {0:<5} {1:>10,.0f} {2:>10.2%} ".format(final_state[0],final_state[1],final_state[2]),3)
	columns("",3,True)	
	for j in range(3): 
		columns(" {0:<5} {1:>10} {2:>10} ".format("="*5,"="*10,"="*10),3)
	print()
	print(center("{0:<18} : {1:>10,.0f}\n" .format("Total Population", sum)))
	print(center("{0:<18} : {1:>10,.0f}" .format("Mean Population", mean_pop)))
	print("\n")
	print(center("{0:^7} : {1:^7}".format("Minutes", "Seconds")))
	print(center("{0:^7.0f} : {1:^7.0f}".format(elapsed_min, elapsed_sec)))
#########################################################################################	
def main():
	clock_timer()
	header()
	lists()
	process()
	output()
#########################################################################################	
def main_bus(repeat = 'y'):
	if repeat == 'n' or repeat == 'N':
		print("\n\n\n")
		print(center('''"Have a nice day!"\n'''))
		input_center("Press <Enter> to continue... ")
		return
	elif repeat == 'y' or repeat == 'Y':
		main()
		repeat = input_center("Would you like to run again (Y/N): ")
		main_bus(repeat)
	else:
		print("\n\n")
		print(center(repeat+" is an invalid entry\n\n"))
		repeat = input_center("Would you like to run again (Y/N): ")
		main_bus(repeat)
#########################################################################################
main_bus()
