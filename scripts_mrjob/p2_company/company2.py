from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        company, price, date = line.split(',')
        try:
            float(price)
        except:
            pass
        else:
            yield company, price

    def reducer(self, company, values):
        l = list(values)
        value_previo = l[0]
        tdc = True
        for i in l[1:]:
            if (value_previo > i):
                tdc = False
                break
            else:
                value_previo = i
        if (tdc):
            yield company, l 

if __name__ == '__main__':
    MRWordFrequencyCount.run()