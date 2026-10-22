using Desmos

state = @desmos begin
    @text "First example"
    @expression cos(x) color=RGB(0, 0.5, 1)
    @expression (cosh(t), sinh(t)) parametric_domain=-2..3
end