'''
Given n books and the ith book has A[i] pages.
You are given k people to copy the n books.

n books list in a row and each person can claim a continous range of the n books.
For example one copier can copy the books from ith to jth continously,
but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

They start copying books at the same time and they all cost 1 minute
to copy 1 page of a book. What's the best strategy to assign books
so that the slowest copier can finish at earliest time?


Example
Given array A = [3,2,4], k = 2.

Return 5( First person spends 5 minutes to copy book 1 and book 2
and second person spends 4 minutes to copy book 3. )
'''
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        if not pages or k <= 0:
            return 0

        start, end = max(pages) ,sum(pages)

        while start + 1 < end:
            mid = start + (end - start) // 2

            if self._count_coiper(pages, mid) <= k:
                end = mid
            else:
                start = mid


        if self._count_coiper(pages, start) <= k:
            return start

        return end


    def _count_coiper(self, pages, time_limit):
        total_pages = 0
        num_of_copier = 0

        for page in pages:
            if total_pages + page > time_limit:
                num_of_copier += 1
                total_pages = page
            else:
                total_pages += page

        num_of_copier += 1

        return num_of_copier


# def main():
#     s = Solution()
#     pages = [13,999,1,2,3,9,11]
#     k = 2
#     print(s.copyBooks(pages, k))
# if __name__ == '__main__':
#     main()
