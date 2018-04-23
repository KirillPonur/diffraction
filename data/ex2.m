
close all
hh=figure;
set(0,'defaultTextInterpreter','latex');
set(0,'DefaultAxesFontSize',12);
set(0,'DefaultTextFontSize',12);
grid on
hold on

%Дельта для красного светофильтра
plot(h_r,delta_r,'r*')
plot(fittedmodel_d_r)
h=200:10:1800;
d_r=4*0.00121*h;
plot(h,d_r)
legend('experiment','cftool','theory')
xlabel('h,mm');
ylabel('$\delta, mm$')
hold off
a_r=0.005524; %угол наклона
epsilon=atan(a_r);
%%%Из паспорта призмы
n=1.52;
alpha=0.002327;
%%%
b=(n-1)*4*alpha; %???????????????????????????
b=num2str(b);
b1='$(n-1)\cdot\alpha=$';
b0=strcat(b1,'',b);
text(500,7.5,b0);
b3=strcat('$\varepsilon=$','',num2str(epsilon));
text(500,7.5,b0);
text(500,7.1,b3);

saveas(hh,'d_r.png')

%Дельта для зелёного светофильтра
hh1=figure;
hold on
grid on
plot(h_g,delta_g,'r*')
plot(fittedmodel_d_g)
h=200:10:1800;
d_g=4*0.00121*h;
plot(h,d_g)
legend('experiment','cftool','theory')
xlabel('h,mm');
ylabel('$\delta$,mm')
hold off
a_r=0.005542; %угол наклона
epsilon=atan(a_r);
%%%Из паспорта призмы
n=1.52;
alpha=0.002327;
%%%
b=(n-1)*4*alpha;
b=num2str(b);
b1='$(n-1)\cdot\alpha=$';
b0=strcat(b1,'',b);
b3=strcat('$\varepsilon=$','',num2str(epsilon));
text(500,7.5,b0);
text(500,7.1,b3);
saveas(hh1,'d_g.png')

%Произведение дельта на d. Красный фильтр
hh2=figure;
hold on
grid on
plot(h_g,delta_d_g,'r*')
plot(fittedmodel_dd_g)
legend('experiment','cftool')
xlabel('$h,mm$');
ylabel('$d\cdot\delta ,mm^2$')
hold off
saveas(hh2,'dd_r.png')
%Произведение дельта на d. Зелёный фильтр
hh3=figure;
hold on
grid on
plot(h_r,delta_d_r,'r*')
plot(fittedmodel_dd_r)
legend('experiment','cftool')
xlabel('$h,mm$');
ylabel('$d\cdot\delta ,mm^2$')
saveas(hh3,'dd_g.png')
