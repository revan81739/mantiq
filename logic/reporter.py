class Reporter:
    def generate(self, argument, valid, counterexample):
        lines=[]

        lines.append("="*40)
        lines.append("MANTIQ")
        lines.append("="*40)
        lines.append("")

        if valid:
            lines.append("RESULT : VALID")
            lines.append("")
            lines.append("Every possible assignment was tested")
            lines.append("No case was found where all premises are true")
            lines.append("and the conclusion is false.")
            lines.append("")
            lines.append("Therefore the conclusion follows logically")
            lines.append("from the premises.")
        else:
            lines.append("RESULT : INVALID")
            lines.append("")
            lines.append("A counterexample was found")
            lines.append("")
            lines.append("In the following assignment:")
            lines.append("")
            lines.append("")
            for variable, value in counterexample.items():
                lines.append(f"{variable}={value}")
            lines.append("")
            lines.append("the premises are all true,")
            lines.append("but the conclusion is false.")
            lines.append("")
            lines.append("Therefore the conclusion")
            lines.append("does not logically follow")
        return "\n".join(lines)



