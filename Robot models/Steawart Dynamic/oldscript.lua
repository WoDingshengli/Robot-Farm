function sysCall_init()
    -- do some initialization here:
    Ktha = math.pi/180 --half angle of hinge point on lower platform
    B_a=34/2.0 --half angle of hinge point on top platform      
    T_a=36.6/2      
    TopR=0.15      
    BottomR=0.234   
    Minlen=0.574    
    EffLen=0.3
    fixlen={}
    stroke={}
    B_Angle={}
    T_Angle={}
    bottomPointX={}
    bottomPointY={}
    bottomPointZ={}
    topPointX={}
    topPointY={}
    topPointZ={}
    
    for i=1,6,1 do
        fixlen[i]=Minlen
        stroke[i]=EffLen
    end

    A={-120,120,0}
    B_Angle[1]=(A[1]+B_a)*Ktha
    B_Angle[2]=(A[1]-B_a)*Ktha
    B_Angle[3]=(A[2]+B_a)*Ktha
    B_Angle[4]=(A[2]-B_a)*Ktha
    B_Angle[5]=(A[3]+B_a)*Ktha
    B_Angle[6]=(A[3]-B_a)*Ktha

    A={-60,180,60}

    T_Angle[1]=(A[1]-T_a)*Ktha
    T_Angle[6]=(A[1]+T_a)*Ktha
    T_Angle[2]=(A[2]+T_a)*Ktha
    T_Angle[3]=(A[2]-T_a)*Ktha
    T_Angle[4]=(A[3]+T_a)*Ktha
    T_Angle[5]=(A[3]-T_a)*Ktha

    Hight=math.sqrt(TopR*TopR+BottomR*BottomR-2*TopR*BottomR*math.cos((60.0-T_a-B_a)*Ktha))
    Hight=math.sqrt((Minlen+EffLen/2)*(Minlen+EffLen/2)-Hight*Hight)
    
    for i=1,6,1 do

        bottomPointX[i]=BottomR*math.cos(B_Angle[i])  
        bottomPointY[i]=BottomR*math.sin(B_Angle[i])  
        bottomPointZ[i]=-Hight

        topPointX[i]=TopR*math.cos(T_Angle[i])  
        topPointY[i]=TopR*math.sin(T_Angle[i])  
        topPointZ[i]=0

    end
    
    givOriX=0
    givOriY=0
    givOriZ=0
    givPosX=0
    givPosY=0
    givPosZ=-Hight

end

P2pLength=function()
    r=(Px-bPX)^2+(Py-bPY)^2+(Pz-bPZ)^2;
    L=math.sqrt(r);
end
legInverseKinematics=function()

    givPosX=position[1]
    givPosY=position[2]
    givPosZ=position[3]
    givOriX=orientation[1]
    givOriY=orientation[2]
    givOriZ=orientation[3]
    length={0,0,0,0,0,0}
    priJoint={0,0,0,0,0,0}
    dh=0 
    sx=math.sin(givOriX*Ktha)
    cx=math.cos(givOriX*Ktha)
    sy=math.sin(givOriY*Ktha)
    cy=math.cos(givOriY*Ktha)
    sz=math.sin(givOriZ*Ktha) 
    cz=math.cos(givOriZ*Ktha)

    tPx={}
    tPy={}
    tPz={}
    bPx={}
    bPy={}
    bPz={}
    giv_len={}

    for i=1,6,1 do

       tPx=topPointX[i]
       tPy=topPointY[i]
       tPz=topPointZ[i]

       Px=cz*cy*tPx+(-cy*sz)*tPy+sy*(tPz-dh)
       Py=(sz*cx+sx*sy*cz)*tPx+(cz*cx-sz*sy*sx)*tPy+(-sx*cy)*(tPz-dh)
       Pz=(sx*sz-cx*sy*cz)*tPx+(sx*cz+cx*sy*sz)*tPy+(cy*cx)*(tPz-dh)

       Px=Px+givPosX
       Py=Py+givPosY
       Pz=Pz+givPosZ+dh

       bPX=bottomPointX[i]
       bPY=bottomPointY[i]
       bPZ=bottomPointZ[i]

       P2pLength()
       length[i]=L-fixlen[i]

       if length[i]>=0 and length[i]<=stroke[i] then
          giv_len[i]=length[i]
       end
       --prismaticJoint[i]=DOF6.cylinder[i].giv_len-0.15
       priJoint[i]=giv_len[i]-0.15
    end
end
function sysCall_actuation()

    t=sim.getSimulationTime()
    -- put your actuation code here
    --
    -- For example:
    --
    -- local position=sim.getObjectPosition(handle,-1)
    -- position[1]=position[1]+0.001
    -- sim.setObjectPosition(handle,-1,position)

    prismaticJoint1=sim.getObjectHandle('Prismatic_joint1')
    prismaticJoint2=sim.getObjectHandle('Prismatic_joint2')
    prismaticJoint3=sim.getObjectHandle('Prismatic_joint3')
    prismaticJoint4=sim.getObjectHandle('Prismatic_joint4')
    prismaticJoint5=sim.getObjectHandle('Prismatic_joint5')
    prismaticJoint6=sim.getObjectHandle('Prismatic_joint6')
    position={0,0,0}
    --orientation={0,30*math.sin(2*math.pi*t),0}
    orientation={0,0,0}
    
    legInverseKinematics()
    --print(priJoint)
    

    sim.setJointTargetPosition(prismaticJoint1,priJoint[1])
    sim.setJointTargetPosition(prismaticJoint2,priJoint[2])
    sim.setJointTargetPosition(prismaticJoint3,priJoint[3])
    sim.setJointTargetPosition(prismaticJoint4,priJoint[4])
    sim.setJointTargetPosition(prismaticJoint5,priJoint[5])
    sim.setJointTargetPosition(prismaticJoint6,priJoint[6])
    --end
    
end

function sysCall_sensing()
    -- put your sensing code here
end

function sysCall_cleanup()
    -- do some clean-up here
end