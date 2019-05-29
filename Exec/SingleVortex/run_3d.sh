rm -rf main3d.gnu.MPI.ex
rm -rf plt*
make DIM=3
mpirun -np 8 ./main3d.gnu.MPI.ex inputs
