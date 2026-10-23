using Desmos
# Desmos
println("ohio have an idea!")

function input(prompt)
    print(prompt)
    return chomp(readline())
end

state = @desmos begin
    @text "Ohio Type Graph"
    @expression cos(x) color=RGB(0, 0.5, 1)
    @expression (cosh(t), sinh(t)) parametric_domain=-2..3
end