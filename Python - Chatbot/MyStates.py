from enum import Enum

class CancelTicket(Enum):
   Start=0
   WAIT_Motive=1
   WAIT_Note = 2

class CloseTicket(Enum):
   Start=0
   WAIT_Journal=1
   WAIT_Close_Note = 2

