# mass,tanb
params = (
	(130, 2),
	(130, 5),
	(130, 10),
	(130, 15),
	(130, 20),
	(130, 25),
	(130, 30),
	(130, 40),
	(130, 50),
	(130, 60),
	(150, 2),
	(150, 5),
	(150, 10),
	(150, 15),
	(150, 20),
	(150, 25),
	(150, 30),
	(150, 40),
	(150, 50),
	(150, 60),
	(170, 2),
	(170, 5),
	(170, 10),
	(170, 15),
	(170, 20),
	(170, 25),
	(170, 30),
	(170, 40),
	(170, 50),
	(170, 60),
	(200, 2),
	(200, 5),
	(200, 10),
	(200, 15),
	(200, 20),
	(200, 25),
	(200, 30),
	(200, 40),
	(200, 50),
	(200, 60),
	(250, 2),
	(250, 5),
	(250, 10),
	(250, 15),
	(250, 20),
	(250, 25),
	(250, 30),
	(250, 40),
	(250, 50),
	(250, 60),
	(300, 2),
	(300, 5),
	(300, 10),
	(300, 15),
	(300, 20),
	(300, 25),
	(300, 30),
	(300, 40),
	(300, 50),
	(300, 60),
	(350, 2),
	(350, 5),
	(350, 10),
	(350, 15),
	(350, 20),
	(350, 25),
	(350, 30),
	(350, 40),
	(350, 50),
	(350, 60),
	(400, 2),
	(400, 5),
	(400, 10),
	(400, 15),
	(400, 20),
	(400, 25),
	(400, 30),
	(400, 40),
	(400, 50),
	(400, 60),
	(450, 2),
	(450, 5),
	(450, 10),
	(450, 15),
	(450, 20),
	(450, 25),
	(450, 30),
	(450, 40),
	(450, 50),
	(450, 60),
	(500, 2),
	(500, 5),
	(500, 10),
	(500, 15),
	(500, 20),
	(500, 25),
	(500, 30),
	(500, 40),
	(500, 50),
	(500, 60),
	(600, 2),
	(600, 5),
	(600, 10),
	(600, 15),
	(600, 20),
	(600, 25),
	(600, 30),
	(600, 40),
	(600, 50),
	(600, 60),
	(700, 2),
	(700, 5),
	(700, 10),
	(700, 15),
	(700, 20),
	(700, 25),
	(700, 30),
	(700, 40),
	(700, 50),
	(700, 60),
	(800, 2),
	(800, 5),
	(800, 10),
	(800, 15),
	(800, 20),
	(800, 25),
	(800, 30),
	(800, 40),
	(800, 50),
	(800, 60),
	(1000, 2),
	(1000, 5),
	(1000, 10),
	(1000, 15),
	(1000, 20),
	(1000, 25),
	(1000, 30),
	(1000, 40),
	(1000, 50),
	(1000, 60),
	(1200, 2),
	(1200, 5),
	(1200, 10),
	(1200, 15),
	(1200, 20),
	(1200, 25),
	(1200, 30),
	(1200, 40),
	(1200, 50),
	(1200, 60),
	(1500, 2),
	(1500, 5),
	(1500, 10),
	(1500, 15),
	(1500, 20),
	(1500, 25),
	(1500, 30),
	(1500, 40),
	(1500, 50),
	(1500, 60),
)


with open("powheg-fh.in_template") as f:
    template = f.read()

for mass, tanb in params: 
    with open("powheg-fh_M{}_tanb{}.in".format(mass, tanb), "w") as f:
        f.write(template.format(mass=mass, tanb=tanb))
