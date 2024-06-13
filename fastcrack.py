from arguments import Arguments
from sshFastCrack.sshFC import sshFastCrack

args = Arguments()
getargs = args.get_arguments()


brute_force = sshFastCrack(getargs)
brute_force.startAttack()