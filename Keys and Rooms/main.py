class Solution(object):
    def recursive(self, rooms, room_num, room_available):
        room_available[room_num] = 1
        for i in rooms[room_num]:
            if room_available[i] != 1:
                self.recursive(rooms, i, room_available)
        return room_available
        
    def canVisitAllRooms(self, rooms):
        room_available= [0] * len(rooms)
        room_available = self.recursive(rooms, 0, room_available)
        
        if 0 in room_available:
            return False
        else:
            return True
                