# Backtracking

This is a tutorial following <www.youtube.com/watch?v=A80YzvNwqXA>.

The general template for solving backtracking solution is noted in ```backtracking_template.py```.

Key Takeaways:
* State: This is a solution for the problem. It can be a valid solution(i.e solution is a correct one) or an invalid state(i.e state doesn't satisfy some problem constraint)

* Template has helper fns. and a main entrypoint that uses the helper fns. In this case(backtracking_template.py), is_valid_state(), get_candidates() and search() are helper functions while solve() is the main entrypoint.