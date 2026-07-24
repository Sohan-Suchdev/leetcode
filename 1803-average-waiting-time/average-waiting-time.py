class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        num_customers = len(customers)
        curr_time = customers[0][0]
        total_wait = 0

        for arrival, time in customers:
            curr_time = max(curr_time, arrival)
            curr_time += time
            total_wait += (curr_time - arrival)

        return total_wait / num_customers
