from __future__ import division  # So we are not using integer division
import sys  # for sys.argv
import fileinput  # to read from file or stdin

streets = {}
points = {}
points2 = {}


def add_point(points, point):
    """
    Add point to a dictionary of the points

    :param points: Dictionary to add to
    :param point: The point to add
    :return: None
    """

    if point not in points:
        points[point] = len(points) + 1


class Street(object):
    def __init__(self, coords):
        self.coords = coords
        #for point in coords:
            #add_point(points, point)

    def __str__(self):
        return ", ".join(str(coord) for coord in self.coords)


def error(message, line):
    """
    Displays an error message to stderr

    :param message: The error message to display
    :param line: The line where the error occurred
    :return: None
    """

    sys.stderr.write("%s:%s\n" % (message, line))


def parse(line):
    """
    Get the name and coordinates from an input line

    :param line: The command line
    :return: name, coordinates
    """

    parts = line.split('"')  # The name is inside " pair
    coords = []  # No coordinates yet
    if len(parts) < 2:  # No name specified
        return None, coords  # No name, No coords
    name = parts[1].strip()
    if len(parts) == 3:  # We have coordinates to process
        for pair in parts[2].split(')'):  # Each coordinate pair
            try:
                if pair:
                    x, y = pair.split(',')  # Remove the ,
                    x = x.strip(" (")
                    point = int(x), int(y)  # Get the x, y coordinates for the point
                    coords.append(point)  # Add the coordinate
            except:
                error("Error in coordinate", pair + ')')
                return name, []  # 1 bad coordinate at least, so return no coordinates
    return name, coords  # name, [coords]


def add(line):
    name, coords = parse(line)
    if not name:
        return "No name specified in add"
    if not coords:
        return "No coordinates specified in add"
    if len(coords) < 2:
        return "No end point in add"
    if name in streets:
        return "Already an existing street called " + name
    streets[name] = Street(coords)


def change(line):
    name, coords = parse(line)
    if not name:
        return "No name specified in change"
    if not coords:
        return "No coordinates specified in change"
    if len(coords) < 2:
        return "No end point in add"
    if name not in streets:
        return "No existing street called " + name
    streets[name] = Street(coords)


# http://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect
def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])


# Return true if line segments AB and CD intersect
def intersect(AB, CD):
    A, B = AB
    C, D = CD
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


# http://stackoverflow.com/questions/20677795/find-the-point-of-intersecting-lines
def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0] * p2[1] - p2[0] * p1[1])
    return A, B, -C


def intersection(segment1, segment2):
    if intersect(segment1, segment2):
        L1 = line(segment1[0], segment1[1])
        L2 = line(segment2[0], segment2[1])

        D = L1[0] * L2[1] - L1[1] * L2[0]
        Dx = L1[2] * L2[1] - L1[1] * L2[2]
        Dy = L1[0] * L2[2] - L1[2] * L2[0]

        if D != 0:
            x = Dx / D
            y = Dy / D
            # Convert back to integer if it is close
            if abs(x - int(x)) < 0.01:
                x = int(x)
            if abs(y - int(y)) < 0.01:
                y = int(y)
            return x, y
        else:
            return None


def graph(line):

    segments = set()
    active = set()
    for name in streets:  # Go through each street
        street = streets[name]  # Get the street
        for segment in zip(street.coords, street.coords[1:]):  # make segments
            # if segment[0] > segment[1]:  # Make sure the segments are smallest x, largest x order
            #    segment = segment[1], segment[0]  # Swap the order of the segment
            segments.add(segment)  # Add it to the list

        intersections = set()
        finals={}
        m=1

        for first in segments:  # Get each pair
            for second in segments:
                ends = set([first[0], first[1], second[0], second[1]])
                if len(ends) == 4:  # There are 4 points, ensure that all are different
                    point = intersection(first, second)  # If there is an intersection create a new point
                    if point:  # If there is an intersection create a new point
                        intersections.add((first[0], point))
                        intersections.add((first[1], point))
                        intersections.add((second[0], point))
                        intersections.add((second[1], point))
                        finals[m]=first[0]
                        finals[m + 1]=first[1]
                        finals[m + 2]=point
                        finals[m + 3]=second[0]
                        finals[m + 4]=second[1]
                        m= m + 4
                        add_point(points, first[0])
                        add_point(points, first[1])
                        add_point(points, point)
                        add_point(points, second[0])
                        add_point(points, second[1])
                        active.add(point)
    print_points = [None] * len(points)

    result={}
    p=1

    for key,value in finals.items():
        if value not in result.values():
            #news.add((value,key,p))
            result[p] = value
            points[value]= p
            p = p + 1


    print '%s%d' % ("V ",int(p))


    for key in active:
        print_points[points[key] - 1] = key

	printintersections1=set()
    printintersections=set()
    onlyintersections= set(active)
    intersectionsunique= set(intersections)

    for segment in intersectionsunique:
        for activep in onlyintersections:
            if(segment[0]==activep or segment[1]== activep):
                printintersections1.add((points[segment[0]], points[segment[1]]))
    for x,y in printintersections1:
        if(x<y):
            m = x
            x = y
            y = m
        printintersections.add((x,y))

    comparestreet=""
    itemstoremove=set()
    for name in streets:  # Go through each street
        street = streets[name]  # Get the street
        x=0
        y=0
        cnt=0
        for segment in zip(street.coords, street.coords[1:]):  # make segments
            for activeint in intersections:
                if(activeint[0]==segment[0] or activeint[0]==segment[1]):
                    for pointofint in onlyintersections:
                        if(pointofint==activeint[1] and cnt==0):
                           x=points[pointofint]
                           cnt = cnt + 1
                        elif(pointofint==activeint[1] and cnt==1):
                            y=points[pointofint]

            if(x!=0 and y!=0):
                if(x!=y):
                    if(x<y):
                        m = x
                        x = y
                        y = m

                    for q,w in printintersections:
                        if(w==y and q>x) or (q==y and q<y) or (q==w):
                            itemstoremove.add((q,w))
                    printintersections.add((x,y))
                    x=0
                    y=0


    try:
        for itemremove in itemstoremove:
            printintersections.remove(itemremove)
    except (RuntimeError, TypeError, NameError):
        pass

    try:
        edgeresults = set(printintersections)
    except (RuntimeError, TypeError, NameError):
        pass

		

    printstring ="E = {"

    try:
        for segment in edgeresults:
            printstring = printstring + "<%d,%d>," % (segment[0], segment[1])
    except (RuntimeError, TypeError, NameError):
        pass

    printstring = printstring[:-1]
    printstring = printstring + "}"
    print printstring


def remove(line):
    name, coords = parse(line)
    if not name:
        return "No name specified in remove"
    if name not in streets:
        return "No existing street called " + name
    del streets[name]  # Remove the street


def unknown(line):
    return "Unknown command"


cmds = {'a': add, 'c': change, 'g': graph, 'r': remove}  # the different commands


def main(args):
    for line in fileinput.input(args):  # read from the file or stdin
        line = line.strip()  # remove the /n at the end of the line
        if line:  # ignore blank lines
            command = cmds.get(line[0], unknown)  # The first character is the command
            message = command(line)  # run the command
            if message:  # if error message, display it
                error(message, line)  # display the error


if __name__ == "__main__":
    main(sys.argv[1:])  # ignore the filename of the python file
