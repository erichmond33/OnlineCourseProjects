import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    



def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )
    
    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # Dictionary that we return
    final_probs = {}
    # Probablities if there is a link vs when there isn't
    nolink_prob = (1 - damping_factor) * (1 / len(corpus))
    yeslink_prob = damping_factor * (1 / len(corpus[page]))
    # Adding either both or one of the probablities
    for pg in corpus.keys():
        final_probs[pg] = nolink_prob
        if pg in corpus[page]:
            final_probs[pg] = nolink_prob + yeslink_prob

    return final_probs


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Returned Dictionary
    final_ranks = {}

    # Random first page
    page = random.choice(list(corpus.keys()))
    # Filling out dictionary with all the possible pages
    for pg in corpus:
        final_ranks[pg] = 0
        # Filling in any empty pages
        if corpus[pg] == set():
            for pg2 in corpus:
                corpus[pg].add(pg2) 

    # Looping n times
    for i in range(n):
        # Calling the transition model then adding one to whatever random choice is made
        page_probs = transition_model(corpus, page, damping_factor)
        choice = random.choices(list(page_probs.keys()), list(page_probs.values()), k=1)
        final_ranks[choice[0]] += 1
        page = choice[0]

    # Calculating the probabilties of each page
    for pg in final_ranks:
        final_ranks[pg] = final_ranks[pg] / n
        
    return final_ranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # A dictionary to store what links go to the key link
    pages_linked_to_page = {}
    # A dictionary for our final ranks
    final_ranks = {}

    # Filling our dictionary with empty sets
    for pg in corpus:
        pages_linked_to_page[pg] = set()

    # Filling the sets with pages that link to each page, and filling final ranks with values of zero
    for pg in corpus:
        for link in corpus:
            if pg in corpus[link]:
                pages_linked_to_page[pg].add(link)
            
        final_ranks[pg] = 0
   
    return iteration_rank(final_ranks, pages_linked_to_page, corpus, damping_factor)


def iteration_rank(final_ranks, pages_linked_to_page, corpus, damping_factor):

    # A vairble to compare to final ranks later
    previous_ranks = final_ranks.copy()
    # A vairble to store values temporarley
    temp_ranks = final_ranks.copy()

    # Vairble to sum the values of links
    summation = 0
    # The iteration rank algorithm
    for page in corpus:
        for link in pages_linked_to_page[page]:
            summation += final_ranks[link] / len(corpus[link])
        temp_ranks[page] = ((1 - damping_factor) / len(corpus)) + (summation * damping_factor)
        summation = 0
    final_ranks = temp_ranks

    # A vairble to see if all the pages haven't changed by .001
    must_be_this_many = 0
    # Checking if each page link's probabilty changed by less than .001
    for rank in final_ranks:
        if final_ranks[rank] - previous_ranks[rank] < .001:
            must_be_this_many += 1
    
    # Checking if we need to run another interation or return
    if must_be_this_many != len(corpus):
        return iteration_rank(final_ranks, pages_linked_to_page, corpus, damping_factor)
    else:
        return final_ranks


if __name__ == "__main__":
    main()
