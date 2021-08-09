F = float(input("推力ton\n"))
pc = float(input("燃焼室圧Mpa\n"))
m = float(input("平均mol質量g/mol\n"))
gamma = float(input("比熱比\n"))
temp = float(input("燃焼速度K\n"))
pe = float(input("ノズル出口圧力Mpa\n"))

ue = (((2*gamma)/(gamma-1))*(8.31/(m*1000))*temp*(1-((pe/pc)**((gamma-1)/gamma))))**(1/2)*1000

cf = (((2*gamma*gamma)/(gamma-1))*(2/(gamma+1))**((gamma+1)/(gamma-1))*(1-((pe/pc)**((gamma-1)/gamma))))**(1/2)

at = F/(cf*pc*100)

myu = (2/(gamma+1))**(1/(gamma-1))/((pe/pc)**(1/gamma)*(((gamma+1)/(gamma-1))*(1-((pe/pc)**((gamma-1)/gamma))))**(1/2))

ae = myu * at

isp = ue / 9.81

m = F*1000/(9.81 * isp)

print("排気速度{}m/s\n推力係数{}\nスロート断面{}m^2\nノズル開口比{}\n出口面積{}m^2\n比推力{}s\n質量流量{}kg/s\n"\
.format(ue, cf, at, myu, ae, isp, m))
