import shelve
import dbm.gnu

def gdbm_shelve(filename, flag="c"):
    return shelve.Shelf(dbm.gnu.open(filename, flag))

db = gdbm_shelve("dbfile")
