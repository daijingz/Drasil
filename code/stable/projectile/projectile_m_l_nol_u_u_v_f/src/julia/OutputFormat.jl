""" OutputFormat.jl
    Provides the function for writing outputs
    - Authors: Samuel J. Crawford, Brooks MacLachlan, and W. Spencer Smith
    - Note: Generated by Drasil v0.1-alpha
"""

module OutputFormat

""" Writes the output values to output.txt
    - Parameter s: output message as a string
    - Parameter d_offset: distance between the target position and the landing position: the offset between the target position and the landing position (m)
    - Parameter t_flight: flight duration: the time when the projectile lands (s)
"""
function write_output(s::String, d_offset::Float32, t_flight::Float32)
    outputfile = open("output.txt", "w")
    print(outputfile, "s = ")
    println(outputfile, s)
    print(outputfile, "d_offset = ")
    println(outputfile, d_offset)
    print(outputfile, "t_flight = ")
    println(outputfile, t_flight)
    close(outputfile)
end

end
