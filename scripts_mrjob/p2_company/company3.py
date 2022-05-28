from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):
  def mapper(self, _, line):
    company,price,date = line.split(',')
    yield date, float(price)

  def reducer(self, date, data):
    dt = list(data)
    avg = sum(dt)/len(dt)
    yield date, avg

if __name__ == '__main__':
  MRWordFrequencyCount.run()