# Jan2026MathCampResources
Resources, homework, etc. for the Math Behind Error Correction camp in January 2026.

## Course Content / Notes

### Day 1

- How to convert numbers from base-10 to base-2
- How to write a number in a different base (ex. $10110_2$)
- How to add numbers in different bases
- Finding the parity of a base-2 string of bits
- Why we need to detect and correct errors
- What the difference is between error detecting and error correcting codes

**Resources**
- [Number base systems](https://math.libretexts.org/Courses/Mount_Royal_University/Higher_Arithmetic/7%3A_Numeration_Systems/7.2%3A_Number_Bases)
- [Modular arithmetic](https://www.geeksforgeeks.org/engineering-mathematics/modular-arithmetic/)
- [Binary arithmetic](https://www.geeksforgeeks.org/digital-logic/arithmetic-operations-of-binary-numbers/#) 

### Day 2

- In general, what codes allow you to detect if an error's occurred
- Repetition code, and why it's inefficient
- Parity and parity in chunks codes, and why you can detect transmission errors but not correct them
- Brainstorm how you could possibly expand these to an error correcting code
- Parity check method used for credit cards (Luhn algorithm)

**Resources**
- [Parity bit method](https://www.geeksforgeeks.org/digital-logic/error-detection-codes-parity-bit-method/) 
- [Luhn algorithm](https://www.geeksforgeeks.org/dsa/luhn-algorithm/)

### Day 3

- 2-dimensional error detection / correction method
- Discuss problems with all the methods we've discussed - we have to assume that there's only been one error
- Brainstorm ideas to detect / correct more than one error
- Small intro to number spaces and set notation, what it means for a number to be within a number space

**Resources**
- [2-dimensional error detection / longitudinal redundancy check](https://www.geeksforgeeks.org/computer-networks/longitudinal-redundancy-check-lrc-2-d-parity-check/)
- [Set notation](https://math.libretexts.org/Courses/Cosumnes_River_College/Corequisite_Codex/01%3A_Sets_and_Numbers/1.02%3A_Sets_and_Set_Notation)

### Day 4

- What are vectors?
	- 1. Describe "hops" on the number line (of real numbers), how to visualize addition as adding "hops" and multiplication as making them longer
	- 2. Now use the coordinate plane, kind of a 2d number line, and how vectors are essentially the 2d version of the "hops"
	- 3. Introduce notation for writing vectors (ex. $\vec{v} = \langle 1, 2 \rangle$)
	- 4. Introduce notation for vector spaces, what vector spaces are, and the ones we'll be using for the rest of the class ($\mathbb{Z}_2^n$)
- Note: vectors themselves are fascinating but addition and multiplication by integers are all the arithmetic we need to know for Hamming codes (no dot products or anything complicated like that)
- This might be enough content for one class?

**Resources**
- [Vectors (lots of notation)](https://math.libretexts.org/Bookshelves/Calculus/Calculus_3e_(Apex)/10%3A_Vectors/10.02%3A_An_Introduction_to_Vectors)
- [Vectors (less notation)](https://mathinsight.org/vector_introduction)
- [Vector spaces (lots of notation)](https://math.libretexts.org/Courses/De_Anza_College/Linear_Algebra%3A_A_First_Course/07%3A_Vector_Spaces/7.01%3A_Vector_Space_-_Definition)
- [Vector spaces (slightly less notation, a bit easier to understand)](https://www.geeksforgeeks.org/maths/basis-and-dimension-in-vector-space/)

### Day 5 / Day 6
- Vector spaces are all possible vectors of a certain length and in a certain base, subspaces are subsets of those. How to define a more restrictive vector subspace as a combination of basis vectors.
- Visual representations of vector spaces and subspaces (squares, cubes, tesseracts, etc.)
- How to tell whether a vector is within a subspace, and why or why not
- Hamming codes - vectors within a subspace are an acceptable message, ones that are just within the space are not.
- Hamming distance between two vectors determines how to correct a message with a transmission error

**Resources**
- [Vector subspaces (lots of notation)](https://textbooks.math.gatech.edu/ila/subspaces.html)
- [Hamming distance / minimum Hamming distance](https://www.geeksforgeeks.org/computer-networks/minimum-hamming-distance/)
- [Hamming space (Wikipedia, couldn't find another source that explains it well)](https://en.wikipedia.org/wiki/Hamming_space)

### Further reading / more interesting resources


- [Error Detection and Correction open course materials from UTAustin](https://www.cs.utexas.edu/~plaxton/c/337/05f/slides/ErrorCorrection-3.pdf)
- [Error Detecting and Correcting Codes - Abstract Algebra open textbook from ASU](https://math.libretexts.org/Bookshelves/Abstract_and_Geometric_Algebra/Abstract_Algebra%3A_Theory_and_Applications_(Judson)/08%3A_Algebraic_Coding_Theory/8.02%3A_Error-Detecting_and_Correcting_Codes)














