
module advect_module

  use amrex_base_module
  use amr_data_module

  implicit none
  private
  
  public :: advect

contains

  subroutine advect(time, lo, hi, &
       &            uin , ui_lo, ui_hi, &
       &            uout, uo_lo, uo_hi, &
       &            vx  , vx_lo, vx_hi, &
       &            vy  , vy_lo, vy_hi, &
       &            flxx, fx_lo, fx_hi, &
       &            flxy, fy_lo, fy_hi, &
       &            dx,dt)

    use compute_flux_module, only : compute_flux_2d

    integer, intent(in) :: lo(2), hi(2)
    real(amrex_real), intent(in) :: dx(2), dt, time
    integer, intent(in) :: ui_lo(2), ui_hi(2)
    integer, intent(in) :: uo_lo(2), uo_hi(2)
    integer, intent(in) :: vx_lo(2), vx_hi(2)
    integer, intent(in) :: vy_lo(2), vy_hi(2)
    integer, intent(in) :: fx_lo(2), fx_hi(2)
    integer, intent(in) :: fy_lo(2), fy_hi(2)
    real(amrex_real), intent(in   ) :: uin (ui_lo(1):ui_hi(1),ui_lo(2):ui_hi(2),ncomp)
    real(amrex_real), intent(inout) :: uout(uo_lo(1):uo_hi(1),uo_lo(2):uo_hi(2),ncomp)
    real(amrex_real), intent(in   ) :: vx  (vx_lo(1):vx_hi(1),vx_lo(2):vx_hi(2))
    real(amrex_real), intent(in   ) :: vy  (vy_lo(1):vy_hi(1),vy_lo(2):vy_hi(2))
    real(amrex_real), intent(  out) :: flxx(fx_lo(1):fx_hi(1),fx_lo(2):fx_hi(2),ncomp)
    real(amrex_real), intent(  out) :: flxy(fy_lo(1):fy_hi(1),fy_lo(2):fy_hi(2),ncomp)
    
    integer :: i, j
    integer :: glo(2), ghi(2)
    real(amrex_real) :: dtdx(2), umax, vmax
    
    real(amrex_real), dimension(:,:), pointer, contiguous :: phix_1d, phiy_1d, phix, phiy, slope
    integer :: icomp

    dtdx = dt/dx
    
    glo = lo - 1
    ghi = hi + 1

    ! edge states
    call amrex_allocate(phix_1d, glo, ghi)
    call amrex_allocate(phiy_1d, glo, ghi)
    call amrex_allocate(phix   , glo, ghi)
    call amrex_allocate(phiy   , glo, ghi)
    ! slope
    call amrex_allocate(slope  , glo, ghi)

    ! We like to allocate these **pointers** here and then pass them to a function
    ! to remove their pointerness for performance, because normally pointers could
    ! be aliasing.  We need to use pointers instead of allocatable arrays because
    ! we like to use BoxLib's amrex_allocate to allocate memeory instead of the intrinsic
    ! allocate.  Amrex_allocate is much faster than allocate inside OMP.  
    ! Note that one MUST CALL AMREX_DEALLOCATE.
    
    ! check if CFL condition is violated.
    umax = maxval(abs(vx))
    vmax = maxval(abs(vy))
    if ( umax*dt .ge. dx(1) .or. &
         vmax*dt .ge. dx(2) ) then
       print *, "umax = ", umax, ", vmax = ", vmax, ", dt = ", dt, ", dx = ", dx
       call amrex_error("CFL violation. Use smaller adv.cfl.")
    end if

    do icomp=1,ncomp

    ! call a function to compute flux
    call compute_flux_2d(lo, hi, dt, dx, &
                         uin(:,:,icomp), ui_lo, ui_hi, &
                         vx, vx_lo, vx_hi, &
                         vy, vy_lo, vy_hi, &
                         flxx, fx_lo, fx_hi, &
                         flxy, fy_lo, fy_hi, &
                         phix_1d, phiy_1d, phix, phiy, slope, glo, ghi,icomp)

    ! Final fluxes
    do    j = lo(2), hi(2)
       do i = lo(1), hi(1)+1
          flxx(i,j,icomp) = phix(i,j) * vx(i,j)
       end do
    end do
    !
    do    j = lo(2), hi(2)+1
       do i = lo(1), hi(1)
          flxy(i,j,icomp) = phiy(i,j) * vy(i,j)
       end do
    end do
    
    ! Do a conservative update
    do    j = lo(2),hi(2)
       do i = lo(1),hi(1)
          uout(i,j,icomp) = uin(i,j,icomp) + &
               ( (flxx(i,j,icomp) - flxx(i+1,j,icomp)) * dtdx(1) &
               + (flxy(i,j,icomp) - flxy(i,j+1,icomp)) * dtdx(2) )
       enddo
    enddo
    
    ! Scale by face area in order to correctly reflx
    do    j = lo(2), hi(2)
       do i = lo(1), hi(1)+1
          flxx(i,j,icomp) = flxx(i,j,icomp) * ( dt * dx(2))
       enddo
    enddo
    
    ! Scale by face area in order to correctly reflx
    do    j = lo(2), hi(2)+1 
       do i = lo(1), hi(1)
          flxy(i,j,icomp) = flxy(i,j,icomp) * (dt * dx(1))
       enddo
    enddo
 
    enddo
    
    call amrex_deallocate(phix_1d)
    call amrex_deallocate(phiy_1d)
    call amrex_deallocate(phix)
    call amrex_deallocate(phiy)
    call amrex_deallocate(slope)
    
  end subroutine advect

end module advect_module
