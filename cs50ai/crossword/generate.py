import sys
import copy

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        # Getting a copy to iterate over
        copy_domains = copy.deepcopy(self.domains)

        # Iterate each vairble object
        for vairble in copy_domains:
            # Iterate each word of that vairble
            for word in copy_domains[vairble]:
                # Delete the ones that aren't the same length as vairble
                if (len(word) != vairble.length):
                    self.domains[vairble].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        # Getting a copy to iterate over
        copy_domains = copy.deepcopy(self.domains)
        # A set for storing all the arc consistent words
        arc_consistent = set()
        # A vairble for the overlaps
        overlaps = self.crossword.overlaps[x, y]

        # If there are no overlaps then it is alreayd arc consistent
        if overlaps == None:
            return False

        # Making sure every word has the same letter where x and y overlap (arc consistency)
        for y_word in copy_domains[y]:
            for x_word in copy_domains[x]:
                if x_word[overlaps[0]] == y_word[overlaps[1]]:
                    arc_consistent.add(x_word)

        # If we don't change anything then it was already arc consistent
        if arc_consistent == self.domains[x]:
            return False

        # Set the the vairble X to the arc_consistent values
        self.domains[x] = arc_consistent
        return True

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # A queue to add and pop arcs from
        queue = []
        # Checking whether we need to add all arcs, or if they were given already
        if arcs==None:
            for var in self.domains:
                for neighbor in self.crossword.neighbors(var):
                    queue.append((neighbor, var))
        else:
            queue = arcs
        # The ac3 algorithim
        while len(queue) != 0:
            arc = queue.pop()
            if self.revise(arc[0], arc[1]):
                if len(self.domains[arc[0]]) == 0:
                    return False
                for neighbor in self.crossword.neighbors(arc[0]):
                    if neighbor != arc[1]:
                        queue.append((neighbor, arc[0]))

        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        ticker = 0
        # Ensuring assigment isn't empty
        if len(assignment) == 0:
            return False
        # Making sure each varible has a value
        for var in assignment:
            if len(assignment[var]) == 0:
                return False
            ticker += 1
        # Making sure all vairbles are present
        if ticker == len(self.domains):
            return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        # Ensuring no repeat assignments
        previous_words = []

        for var in assignment:
            if assignment[var] in previous_words:
                return False
            previous_words.append(assignment[var])

        # Ensuring lenght requirements
        for vairble in assignment:
            for word in self.domains[vairble]:
                if (len(word) != vairble.length):
                    return False

        # Ensuring neighbor requirements
        queue = []
        for var in assignment:
            for neighbor in self.crossword.neighbors(var):
                if neighbor in assignment:
                    queue.append((neighbor, var))

        for x,y in queue:
            overlaps = self.crossword.overlaps[x, y]
            if assignment[x][overlaps[0]] != assignment[y][overlaps[1]]:
                return False

        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        final_domains = dict()
        copy_domains = copy.deepcopy(self.domains)
        # Getting rid of tha varibles that are already assigned
        for varible in self.domains:
            if varible in assignment:
                del copy_domains[varible]
        # Couting how many times a domain appears in other's domains
        for domain in copy_domains[var]:
            final_domains[domain] = 0
            for varible in copy_domains:
                if domain in copy_domains[varible]:
                    final_domains[domain] += 1
        # Sorting
        final_domains = dict(sorted(final_domains.items(), key=lambda item: item[1]))
        # Dict ---> List
        final_domains = list(final_domains)

        return final_domains

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        current_lowest = 1000
        tied_lowest = []

        copy_domains = copy.deepcopy(self.domains)
        # Getting rid of tha varibles that are already assigned
        for varible in self.domains:
            if varible in assignment:
                del copy_domains[varible]

        # Finding the varibles with the fewest domains left
        for var in copy_domains:
            if len(copy_domains[var]) == current_lowest:
                tied_lowest.append(var)
            elif len(copy_domains[var]) < current_lowest:
                tied_lowest.clear()
                tied_lowest.append(var)
                current_lowest = len(copy_domains[var])

        # Out of the varibles that tied with the fewest domains... finding the one with the most neighbors
        final_biggest = tied_lowest[0]
        for var in tied_lowest:
            if len(self.crossword.neighbors(var)) > len(self.crossword.neighbors(final_biggest)):
                final_biggest = var
        return(final_biggest)

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        # Base case
        if self.assignment_complete(assignment) == True:
            return assignment
        # Selecting var
        var = self.select_unassigned_variable(assignment)
        # The rest of backtrack...
        for value in self.order_domain_values(var, assignment):
            assignment[var] = value
            if self.consistent(assignment):
                result = self.backtrack(assignment)
                if result != None:
                    return result
                
            del assignment[var]
        return None

        
def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
