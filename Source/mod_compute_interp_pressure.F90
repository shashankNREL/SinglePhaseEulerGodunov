module mod_compute_interp_pressure

  use amrex_base_module
  use amrex_amr_module
  use amr_data_module
  use fillpatch_module

  implicit none

contains

subroutine compute_interp_pressure

    implicit none

    integer :: ilev
    integer :: prlo(4), prhi(4), borlo(4), borhi(4), fxlo(4), fxhi(4), fylo(4), fyhi(4), fzlo(4), fzhi(4)
    type(amrex_box) :: bx
    type(amrex_mfiter) :: mfi
    real(amrex_real), contiguous, dimension(:,:,:,:), pointer :: PXptr, PYptr, PZptr, Pptr, phiborderptr
    integer :: nlevs
    integer, parameter :: ngrow = 3
    type(amrex_multifab) :: phiborder
    real(amrex_real) :: time
	
    time=0.0d0

    nlevs = amrex_get_finest_level()

    do ilev = 0, nlevs

       call amrex_multifab_build(phiborder, phi_new(ilev)%ba, phi_new(ilev)%dm, ncomp, ngrow)
       call fillpatch (ilev, time, phiborder, phi_mp, phi_mp)

       call amrex_mfiter_build(mfi, phi_new(ilev), tiling=.true.)
       do while (mfi%next())
          bx = mfi%tilebox()
 	  Pptr 	       => Pmfab(ilev)%dataptr(mfi)
 	  phiborderptr => phiborder%dataptr(mfi)
	  PXptr      => Pfacemfab(1,ilev)%dataptr(mfi)
	  PYptr      => Pfacemfab(2,ilev)%dataptr(mfi)
	  PZptr      => Pfacemfab(3,ilev)%dataptr(mfi)
	  borlo  = lbound(phiborderptr)
	  borhi  = ubound(phiborderptr)
          prlo   = lbound(Pptr)
          prhi   = ubound(Pptr)
	  fxlo    = lbound(PXptr)
	  fxhi    = ubound(PXptr)
	  fylo    = lbound(PYptr)
	  fyhi    = ubound(PYptr)
	  fzlo    = lbound(PZptr)
	  fzhi    = ubound(PZptr)

        call interp_pressure(ilev, bx%lo, bx%hi, phiborderptr(:,:,:,1), borlo, borhi, PXptr,&
  	       fxlo,fxhi,PYptr,fylo,fyhi,PZptr,fzlo,fzhi,Pptr,prlo,prhi,amrex_geom(ilev)%dx, amrex_problo)

       end do
       call amrex_mfiter_destroy(mfi)
     
       call amrex_multifab_destroy(phiborder)

    end do

end subroutine compute_interp_pressure

subroutine interp_pressure(level, lo, hi, &
     RHO, borlo, borhi, PX,&
     fxlo, fxhi, PY, fylo, fyhi, PZ, fzlo, fzhi, P, prlo, prhi, dx, prob_lo)

  implicit none
  integer, intent(in) :: level, lo(3), hi(3), prlo(3), prhi(3), borlo(3), borhi(3), fxlo(3), fxhi(3), fylo(3), fyhi(3), fzlo(3), fzhi(3)
  double precision, dimension(borlo(1):borhi(1),borlo(2):borhi(2),borlo(3):borhi(3)) :: RHO
  double precision, dimension(prlo(1):prhi(1),prlo(2):prhi(2),prlo(3):prhi(3)) :: P
  double precision, dimension(fxlo(1):fxhi(1),fxlo(2):fxhi(2),fxlo(3):fxhi(3)) :: PX
  double precision, dimension(fylo(1):fyhi(1),fylo(2):fyhi(2),fylo(3):fyhi(3)) :: PY
  double precision, dimension(fzlo(1):fzhi(1),fzlo(2):fzhi(2),fzlo(3):fzhi(3)) :: PZ

  double precision, intent(in) :: dx(3), prob_lo(3)
  integer          :: i,j,k
  double precision :: x,y,z

  do k=lo(3),hi(3)
     do j=lo(2),hi(2)
        do i=lo(1),hi(1)+1
    	   PX(i,j,k) = (P(i-1,j,k)*RHO(i,j,k)+P(i,j,k)*RHO(i-1,j,k))/(RHO(i-1,j,k)+RHO(i,j,k))
        end do
     end do
  end do

  do k=lo(3),hi(3)
     do j=lo(2),hi(2)+1
        do i=lo(1),hi(1)
    	   PY(i,j,k) = (P(i,j-1,k)*RHO(i,j,k)+P(i,j,k)*RHO(i,j-1,k))/(RHO(i,j-1,k)+RHO(i,j,k))
        end do
     end do
  end do

  do k=lo(3),hi(3)+1
     do j=lo(2),hi(2)
        do i=lo(1),hi(1)
    	   PZ(i,j,k) = (P(i,j,k-1)*RHO(i,j,k)+P(i,j,k)*RHO(i,j,k-1))/(RHO(i,j,k-1)+RHO(i,j,k))
        end do
     end do
  end do


end subroutine interp_pressure
 
end module mod_compute_interp_pressure
