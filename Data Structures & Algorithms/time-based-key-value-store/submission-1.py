class TimeMap:

    def __init__(self):
        self.key_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_dict:
            self.key_dict[key] = []
        self.key_dict[key].append([timestamp, value])


    def get(self, key: str, timestamp: int) -> str:
       
        if key not in self.key_dict:
            return ""
        value = self.key_dict[key]
        l,r=0, len(self.key_dict[key])-1
        res=""

        while l<=r:
            mid = (l+r)//2
            mid_time, mid_val =value[mid]
            if mid_time<= timestamp:
                l=mid+1
                res= mid_val
            else:
                r= mid-1
        return res

        
