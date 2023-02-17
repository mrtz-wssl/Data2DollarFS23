import twint

c = twint.Config()
c.Username = "ABack"
c.Output = "hey.csv"

twint.run.Search(c)



