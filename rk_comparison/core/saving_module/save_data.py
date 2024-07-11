from csv import writer

class SaveData:

    def save(self, file, controller):
        w = writer(file)

        data = self.prepare_data(controller)
        l = []
        n = len(data[0])
        m = len(data)
        for j in range(n):
            for i in range(m):
                l.append(data[i][j])
            w.writerow(l)
            l = []

    def prepare_data(self, controller):
        results = [[controller.descriptions[-1]] + controller.rs.get_result_analytical()]

        return results
